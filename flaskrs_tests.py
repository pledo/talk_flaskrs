import os
import flaskrs
import unittest
import tempfile

class FlaskrsTestCase(unittest.TestCase):
#    def __init__(self,  ):
#        pass
    def setUp(self):
        """docstring for setUp"""
        self.db_fd, flaskrs.app.config['DATABASE'] = tempfile.mkstemp()
        flaskrs.app.config['TESTING'] = True
        self.app = flaskrs.app.test_client()
        flaskrs.init_db()

    def tearDown(self):
        """docstring for tearDown"""
        os.close(self.db_fd)
        os.unlink(flaskrs.app.config['DATABASE'])

    def test_empty_db(self):
        """docstring for test_empty_db"""
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

    def login(self, username, password):
        """docstring for login"""
        return self.app.post('/login', data=dict(
            username=username, password=password),
        follow_redirects=True)

    def logout(self):
        """docstring for logout"""
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        """docstring for test_login_logout"""
        rv = self.login('admin', 'default')
        assert 'You were logged in' in rv.data
        rv = self.logout()
        assert 'You were logged out' in rv.data
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in rv.data
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in rv.data

    def test_messages(self):
        """docstring for test_messages"""
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(
            title='<Hello>', text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert 'No entries here so far' not in rv.data
        assert '&lt;Hello&gt;' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data
#-------------------------
if __name__ == '__main__':
    unittest.main()
