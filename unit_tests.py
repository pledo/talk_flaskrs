#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import flaskrs
#import talk_flaskrs
import pytest

def test_db_connection():
    """docstring for test_db_connection"""
    assert flaskrs.connect_db()
