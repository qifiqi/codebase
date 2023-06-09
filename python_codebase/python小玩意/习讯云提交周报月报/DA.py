# -*- coding: utf-8 -*-
import requests

USER = '17752825932'
PASSWORD = 'lym011013..'
SCHOOL_ID = 542

LOG_PUBLIC = 'https://api.xixunyun.com/'

LOGIN_URL = LOG_PUBLIC + 'login/admin'

LOGOUT_URL = LOG_PUBLIC + 'login/logout'

HEADER = {
  "content-type": "application/x-www-form-urlencoded",
  "User-Agent": "okhttp/3.8.1",
}

SESSIONS = requests.Session()
SESSIONS.headers = HEADER
