#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import exit
from time import sleep
from requests import get

url = 'http://localhost:5000'
text_home = 'Flaskr'
brow_name= 'firefox'
sleep_time = 6

def t_home(url):
    """docstring for setUp"""
    print('Inside in the test_home function')
    result = get(url)
    print(result.status_code)
    if result.status_code == 200:
        print("Home Ok")
        return(0)
    else:
        print("Home Fail")
        return(1)


def t_login(browser_obj):
    """docstring for test_login"""
    pass

def main():
    """docstring for main"""
    print("Inside in the main function")
    res = t_home(url)
    return(res)

if __name__ == '__main__':
    exit(main())
