from flask import Flask

app = Flask(__name__)
#app.config.from_envvar('FETCHWEB_SETTINGS')

import fetchweb.views
