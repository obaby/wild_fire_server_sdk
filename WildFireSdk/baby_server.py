import hashlib
import random
import time

import requests as rq
import json

# obaby@mars
# by:obaby
# http://www.h4ck.org.cn
# http://www.obaby.org.cn
# http://www.findu.co

class BabyServer():

    def __init__(self,
                 host,
                 http_port,
                 port,
                 websocket_port,
                 secret_key,
                 token_key,
                 debug=False,
                 timeout=5,
                 json_response=True):
        self.host = host
        self.http_port = http_port
        self.websocket_port = websocket_port
        self.port = port
        self.secret_key = secret_key
        self.token_key = token_key
        self.debug = debug
        self.timeout = timeout
        self.json_response = json_response

    def baby_post(self, url, data):
        # data = {'id': 123}
        data = json.dumps(data)
        nonce = random.randrange(1000000, 10000000)
        # sign = sha1(nonce + "|" + SECRET_KEY + "|" + timestamp)
        timestamp = int(time.time()) * 1000
        sign = hashlib.sha1(str(str(nonce) + "|" + self.secret_key + "|" + str(timestamp)).encode('utf8')).hexdigest()
        headers = {'content-type': 'application/json',
                   'timestamp': str(timestamp),
                   'nonce': str(nonce),
                   'sign': sign}
        try:
            res = rq.post(url=url, data=data, headers=headers, timeout=self.timeout)
        except Exception as e:
            print(e)
            return None
        if self.debug:
            print("[*] Headers:", headers)
            print('[*] Url:', url)
            print("[*] Resp StatusCode:", res.status_code)
            print("[*] Resp Text:", res.text)
        if self.json_response:
            try:
                resp = res.json()
                return resp
            except Exception as e:
                print(e)
            return None
        else:
            return res.text

    def format_request_url(self, path):
        return 'http://' + self.host + ':' + self.port + path

    def print_info(self):
        print('*' * 100)
        print('Wild fire server python sdk v1.0\r\n')
        print('http://www.h4ck.org.cn')
        print('http://www.obaby.org.cn')
        print('http://www.findu.co')
        print('By: obaby')
        print('obaby@mars')
        print('*' * 100)


if __name__ == '__main__':
    bs = BabyServer(host='123.60.47.163',
                    http_port='80',
                    port='18080',
                    websocket_port='8083',
                    secret_key='123456',
                    token_key='',
                    debug=True)
    bs.print_info()
