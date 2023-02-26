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
mycursor = conn.cursor()


# Creates the client table for APP
# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint, userID int PRIMARY KEY AUTO_INCREMENT)")

# Test Input for eventual Front-implementation
user_name = input("Input your Name: ")
user_age = int(input("Input your Age:"))

mycursor.execute("DROP table person")
conn.commit()
# # Run SQL for database
# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", (user_name, user_age))

# # Commit changes from SQL command to database
# conn.commit()

# mycursor.execute("SELECT * from Person")

# for x in mycursor:
#   print(x)