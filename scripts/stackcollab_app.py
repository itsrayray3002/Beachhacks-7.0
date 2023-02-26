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
mycursor.execute("SELECT * FROM User")
# mycursor.execute("SHOW DATABASES")

# print the results
for row in mycursor:
   print(row)

class User(db.Model):
   # id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(120), primary_key=True)
   
   # new fields for profile
   fname = db.Column(db.String(80), unique=False)
   age = db.Column(db.Integer, unique=False)
   bio = db.Column(db.String(240), unique=False)
   github = db.Column(db.String(80), unique=True)


   def __repr__(self):
      return '<Task %r>' % self.id

# db.create_all()


@app.route('/', methods=['POST', 'GET'])
def index():
   if request.method == 'POST':
      users = mycursor.execute("SELECT * FROM User WHERE email = '%s'" % request.form['email'])
      if users == None:
         user = None
      else:
         user = users.first()
         

      if user is None:
         print("User not found, creating!")
         user = User(email=request.form['email'], fname=request.form['fname'], age=request.form['age'], bio=request.form['bio'], github=request.form['github'])
         try:
            db.session.add(user)
            db.session.commit()  # update the user in the database
            return redirect('/')
         except Exception as e:
            return 'There was an issue saving your profile information to the database... Please try again later. Error message:\n' + str(e)
      else:
         print("User found, updating!")
         user.fname = request.form['fname']
         user.age = request.form['age']
         user.bio = request.form['bio']
         user.github = request.form['github']

         try:
            db.session.update(user)
            db.session.commit()  # update the user in the database
            return redirect('/')
         except:
            return 'There was an issue saving your profile information to the database... Please try again later.'
   else:
        profile = {'fname': 'John', 'age': 30, 'bio': 'I like to play football', 'tags': ['football', 'basketball', 'tennis']}
        return render_template("profile.html", profile=profile)

@app.route('/background_process_test')
def background_process_test():
   return("nothing")

if __name__ == "__main__":
    app.run(debug=True)

