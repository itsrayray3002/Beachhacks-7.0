import os
from flask import Flask, render_template, request, url_for, redirect
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


app = Flask(__name__)
# Configuring and Accessing the Database
# mysql_obj = MySQL()
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lWGTQm32UWinY8GqQzby@localhost/sql_test'

db.init_app(app)


# create a cursor
mysql_connector = mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="lWGTQm32UWinY8GqQzby")
mycursor = mysql_connector.cursor()

# execute a query
mycursor.execute("USE sql_test")
mycursor.execute("SELECT * FROM Person")
# mycursor.execute("SHOW DATABASES")

# print the results
for row in mycursor:
   print(row)

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True)
   email = db.Column(db.String(120), unique=True)

   def __repr__(self):
      return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
    #   task_content = request.form['content']
    #   new_task = User(cont)
        pass
    else:
         profile = {'name': 'John', 'age': 30, 'bio': 'I like to play football', 'tags': ['football', 'basketball', 'tennis']}
         return render_template("swipe.html", profile=profile)

@app.route('/background_process_test')
def background_process_test():
   return("nothing")

if __name__ == "__main__":
    app.run(debug=True)

