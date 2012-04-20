from flask import request, session, g, redirect, url_for, render_template
from fetchmusic import app, query_db, connect_db

@app.before_request
def before_request():
    """Make sure we are the connected to the database each request and look
    up the current user to make sure they are connected
    """
    g.db = connect_db()
    g.user = None
    if 'uid' in session:
        g.user = query_db('select * from users where uid = ?',
                          [session['uid']], one=True)

@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Logs the user in."""
    if g.user:
        return redirect(url_for('home'))
    error = None
    if request.method == 'POST':
        user = query_db('''select * from users where 
            email = ?''', [request.form['email'].lower()], one=True)
        if user is None:
            error = 'Invalid email'
        elif not check_password_hash(user['pw_hash'],
                                     request.form['password']):
            error = 'Invalid password'
        else:
            session['uid'] = user['uid']
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout', methods=['POST'])
def logout():
    """Logs user out."""
    flash('you were logged out.')
    session.pop('uid', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Registers the user. """
    if g.user:
        return redirect(url_for('home'))
    error = None
    if request.method == 'POST':
        if not request.form['username']:
            error = "You have to enter a username."
        elif not request.form['email'] or \
                '@' not in request.form['email']:
            error = "You have to enter a valid email."
        elif not request.form['password']:
            error = "You have to enter a password."
        elif request.form['password'] != request.form['password2']:
            error = "The two passwords do not match."
        elif get_user_id(request.form['email']) is not None:
            error = "User with this email already exists."
        else:
            g.db.execute('''insert into pending_users (
                username, email, pw_hash) values (?, ?, ?)''',
                [request.form['username'], request.form['email'],
                 generate_password_hash(request.form['password'])])
            g.db.commit()
            return redirect(url_for('login'))
    return render_template('register.html', error=error)


@app.route('/')
def home():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('index.html', username=g.user['username'],
                           fetches=fetches, name="home")
