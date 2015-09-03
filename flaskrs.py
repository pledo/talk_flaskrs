# all the imports
import sqlite3
from flask import Flask, request, session, g,\
    redirect, url_for, abort, render_template,\
    flash
from contextlib import closing

# configuration

DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# Create our little application
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    """docstring for connect_db"""
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    """docstring for init_db"""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    """docstring for before_request"""
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    """docstring for teardown_request"""
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

# A funcao abaixo ira mostrar as entradas, ou seja, os posts
#Sera uma pilha, a entrada mais nova estara
#no topo
@app.route('/')
def show_entries():
    """docstring for show_entries"""
#    init_db()
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
#    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

#A funcao abaixo irapermitir que um user logado
#Adicione novas entradas. Ela apenas responde a
#requisicoes POST. Apos adicionar a entrada
#A aplicacao ira rodar um flash no navegador
# e mostrar novamente as entradas
# Ela primeiro verifica se o use esta logado, caso nao
#retorna um 401.
#Caso sim, abre o console para a adicao da entrada
# e depois da um refresh na pagina
@app.route('/add', methods=['POST'])
def add_entry():
    """docstring for add_entry"""
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('Insert into entries (title, text) values (?, ?)',
        [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """docstring for login"""
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    """docstring for logout"""
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
#---------------------------------

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')
