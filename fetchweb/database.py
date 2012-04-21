from contextlib import closing
from fetchweb import app
from flask import g
from sqlite3 import dbapi2 as sqlite3

def connect_db():
    """Creates a global connection to the database."""
    return sqlite3.connect(app.config['DATABASE_PATH'])

def refresh_db():
    """Deletes Old, Creates the database tables."""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    """Queries the database and returns a list of dictionaries."""
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv

def get_user_id(email=None, username=None):
    """ retrieves user_id associated with email. """
    if email and username:
        rv = g.db.execute('select uid from users where email = ? and username=?',
                      [email, username]).fetchone()
    elif email:
        rv = g.db.execute('select uid from users where email = ?', [email]).fetchone()
    elif username:
        rv = g.db.execute('select uid from users where username = ?', [username]).fetchone()
    else:
        return None
    return rv[0] if rv else None