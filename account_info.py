# coding : utf-8

import os


class Account:
    email = ''
    password = ''

    def __init__(self):
        self.email = os.environ['EMAIL']
        self.password = os.environ['PASS']


