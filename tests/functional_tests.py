#!/usr/bin/env python
# -*- coding: utf-8 -*-

from splinter import Browser
from sys import exit
from time import sleep

url = 'http://localhost:5000'
url_login = 'http://localhost:5000/login'
text_home = 'Flaskr'
brow_name= 'firefox'
sleep_time = 6

def start_browser(browser_name):
    print("Inside in the start_browser function")
    print('Start Browser')
    browser = Browser(browser_name)
    return(browser)

def t_home(browser_obj, address_url):
    """docstring for setUp"""
    print('Inside in the test_home function')
#    browser = Browser('firefox')
    print('Enter in the home')
    browser_obj.visit(address_url)
    result = browser_obj.is_text_present(text_home)
    if result:
        print("Home Ok")
    else:
        print("Home Fail")
    sleep(sleep_time)
    browser_obj.quit()
    return(result)


def t_login(url_l):
    """docstring for test_login"""
    with Browser() as browser_obj:
        browser_obj.visit(url_l)
        browser_obj.fill('username', 'admin')
        browser_obj.fill('password', 'default')
        button = browser_obj.find_by_value('Login')
        if button.is_empty != False:
            button.click()
            print("Login Ok")
            sleep(sleep_time)
            #browser_obj.quit()
            return(0)
        else:
            print("Login Fail")
            sleep(sleep_time)
            #browser_obj.quit()
            return(1)

def main():
    """docstring for main"""
    print("Inside in the main function")
    br = start_browser(brow_name)
    t_home(br, url)
    br = start_browser(brow_name)
    t_login(url_login)

if __name__ == '__main__':
    exit(main())
