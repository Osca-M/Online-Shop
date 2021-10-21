# Django Oauth2 (Client Credentials grant)
This project exposes a REST API for authentication. It is created on Django, djangorestframework and 0auth2. By default,
the supported database is PostgreSQL, you can however switch to a database of your choice by tweaking the database
section in the production settings file.

To run the application; clone the repository, create a <code>.env</code> file in the project root directory add the
following environment variables.
<code>
PROD_DB_NAME={database name} <br>
PROD_DB_USER={database user} <br>
PROD_DB_PASSWORD={database password} <br>
PROD_DB_HOST={database host} <br>
PROD_DB_PORT={database port}
</code>
<br>
Regards the database, my assumption is that your database has a public schema.
