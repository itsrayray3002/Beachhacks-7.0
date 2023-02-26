import os
from flask import Flask, render_template, request, url_for, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
# Configuring and Accessing the Database
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'lWGTQm32UWinY8GqQzby'
app.config['MYSQL_DATABASE_DB'] = 'sql_test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# create a cursor
conn = mysql.connect()
mycursor =conn.cursor()

# execute a query
mycursor.execute("SELECT * FROM customers")

mycursor.



