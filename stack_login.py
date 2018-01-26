# coding : utf-8

from account_info import Account
import requests
import re
import datetime


class StackOverflow:
    base_url = 'https://stackoverflow.com/users/login'
    fkey = ''

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }

    params = {
        "ssrc": "head",
        "returnurl": "https://stackoverflow.com/",
    }

    def login(self):
        session = requests.session()
        print('Start login ...')
        account = Account()
        print('Email : {}\nPassword : {}'.format(account.email, account.password))
        payload = self.get_payload(account)
        response = session.post(self.base_url, data=payload, headers=self.headers, params=self.params)
        if response.history:
            print("\033[92mLogged in:{} with fkey: {}\033[0m".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                                                                     payload['fkey']))
        else:
            print("\033[91mPlease check your email and password."
                  "If nothing wrong, please report this issue to https://github.com/CoXier/stackoverflow-login/issues\033[0m")
        # Only for continuous login
        r = session.get("https://stackoverflow.com/")

    def get_fkey(self):
        print('Retrieving fkey information...')
        response = requests.get(self.base_url, params=self.params, headers=self.headers)
        return re.search(r'"fkey":"([^"]+)"', response.text).group(1)

    def get_payload(self, account):
        self.fkey = self.get_fkey()
        return {
            'openid_identifier': '',
            'password': account.password,
            'fkey': self.fkey,
            'email': account.email,
            'oauth_server': '',
            'oauth_version': '',
            'openid_username': '',
            'ssrc': 'head',
        }


if __name__ == '__main__':
    stack_overflow = StackOverflow()
    stack_overflow.login()
