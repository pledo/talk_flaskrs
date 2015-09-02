#!/usr/bin/env python
# -*- coding: utf-8 -*-

from splinter import Browser
from sys import exit
from time import sleep

url = 'http://localhost:5000'
text_home = 'Flaskr'
brow_name= 'firefox'
sleep_time = 6

def start_browser(browser_name):
    print("Inside in the start_browser function")
    print('Start Browser')
    browser = Browser(browser_name)
    return(browser)

def test_home(browser_obj, address_url):
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


def test_login(browser_obj):
    """docstring for test_login"""
    pass

def main():
    """docstring for main"""
    print("Inside in the main function")
    br = start_browser(brow_name)
    test_home(br, url)

if __name__ == '__main__':
    exit(main())
