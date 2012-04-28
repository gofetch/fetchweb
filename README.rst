fetch music
===========

Example Usage
-------------

First, install the fetchweb package and its dependencies.

Create a configuration.cfg defining the two following values::

  DATABASE_PATH = '/path/to/fetchweb.db'
  SECRET_KEY = 'DEVELOPMENT KEY'

Export the variable FETCHWEB_SETTINGS::

  export FETCHWEB_SETTINGS=/path/to/configuration.cfg

If needed, initialize the database by running schema.sql::

  from fetchweb.database import refresh_db; refresh_db()

Serve the application from python or other server::

  from fetchweb import app
  app.run(debug=True, host="localhost", port=5000)

