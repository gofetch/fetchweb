import database
from flask import flash, g, redirect, render_template, request, session, url_for
from fetchweb import app
from werkzeug import check_password_hash, generate_password_hash

@app.before_request
def before_request():
    """Make sure we are the connected to the database each request and look
        up the current user to make sure they are connected
        """
    g.db = database.connect_db()
    g.user = None
    if 'uid' in session:
        g.user = database.query_db('select * from users where uid = ?',
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
    if request.method == 'POST':
        user = database.query_db('''select * from users where 
            email = ?''', [request.form['email'].lower()], one=True)
        if user is None:
            flash('Invalid email')
        elif not check_password_hash(user['pw_hash'],
                                     request.form['password']):
            flash('Invalid password')
        else:
            session['uid'] = user['uid']
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logs user out."""
    flash('You were logged out.')
    session.pop('uid', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Registers the user. """
    if g.user:
        return redirect(url_for('home'))
    if request.method == 'POST':
        if not request.form['username']:
            flash("You have to enter a username.")
        elif not request.form['email'] or '@' not in request.form['email']:
            flash("You have to enter a valid email.")
        elif not request.form['password']:
            flash("You have to enter a password.")
        elif request.form['password'] != request.form['password2']:
            flash("The two passwords do not match.")
        elif database.get_user_id(email=request.form['email']) is not None:
            flash("User with this email already exists.")
        elif database.get_user_id(username=request.form['username']) is not None:
            flash("User with this username already exists.")
        else:
            g.db.execute('''insert into pending_users (
                username, email, pw_hash) values (?, ?, ?)''',
                         [request.form['username'], request.form['email'],
                          generate_password_hash(request.form['password'])])
            g.db.commit()
            flash("Successfully requested an account");
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/')
def home():
    if not g.user:
        return redirect(url_for('login'))
    else:
        return redirect(url_for('locker', category='music'))

@app.route('/<category>')
def locker(category):
    '''Homepage'''
    if not g.user:
        return redirect(url_for('login'))
    # TODO(tal): list of fetches
    fetches = []
    return render_template("index.html", username=g.user['username'],
                           category=category, fetches=fetches)

@app.route('/search/music')
def music():
    ''' Shows the main music page '''
    if not g.user:
        return redirect(url_for('login'))
    if request.args.get('query'):
        query = request.args.get('query')
        # query whatapi, get back result
        # return render_template('music-search.html')
        # TODO(tal)
        raise NotImplementedError
    else:
        return render_template('music-landing.html')


@app.route('/music/artist')
def artist():
    ''' show the artist page. '''
    raise NotImplementedError
