# coding : utf-8

import os
import json


class Account:
    email = ''
    password = ''

    def __init__(self):
        current_dir = os.path.dirname(__file__)
        json_file = os.path.join(current_dir, 'config/account.json')
        json_data = json.load(open(json_file))
        self.email = json_data.get('email')
        self.password = json_data.get('password')


