from flask import Flask, g
from sqlite3 import dbapi2 as sqlite3

app = Flask(__name__)
app.config.from_envvar('FETCHMUSIC_SETTINGS', silent=True)


import fetchmusic.views

