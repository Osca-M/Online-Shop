# Django Oauth2 (Client Credentials grant)
This project exposes a REST API for authentication. It is created on Django, djangorestframework and 0auth2. By default,
the supported database is PostgreSQL, you can however switch to a database of your choice by tweaking the database
section in the production settings file.

To run the application; clone the repository, create a <code>.env</code> file in the project root directory add the
following environment variables.
<br>
`PROD_DB_NAME={database name}` <br>
`PROD_DB_USER={database user}` <br>
`PROD_DB_PASSWORD={database password}` <br>
`PROD_DB_HOST={database host}` <br>
`PROD_DB_PORT={database port}`

<br>
Regards the database, my assumption is that your database has a public schema.

Install the project requirements `pip install -r requirement.txt`
<br><br>
Apply the database migrations to your database `python manage.py migrate`
<br><br>
You can now run the django server `python manage.py runserver 0.0.0.0:5603`
<br><br>

The REST API Endpoints can be accessed from:
<br><br>
`0.0.0.0:8000/auth/create-account`<br>
To create a user
<br><br>
`0.0.0.0:8000/auth/login`<br>
For login
<br><br>
`0.0.0.0:8000/auth/refresh-token`<br>
To refresh access tokens
<br><br>
`0.0.0.0:8000/auth/logout`<br>
Invalidate access tokens
<br><br>
`0.0.0.0:8000/auth/change-password`<br>
Change password for a user
<br><br>
`0.0.0.0:8000/auth/profile`<br>
Get a user's profile. Method POST
<br><br>
`0.0.0.0:8000/auth/profile`<br>
Update a User's profile. Method PUT.