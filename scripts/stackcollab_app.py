import os
from flask import Flask, render_template, request, url_for, redirect
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
#from flask_login import login_required, current_user, login_user
#from flask_dance.consumer import OAuth2ConsumerBlueprint
#rom flask_dance.consumer.storage.sqla import SQLAlchemyStorage

app = Flask(__name__)
# Configuring and Accessing the Database
# mysql_obj = MySQL()
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lWGTQm32UWinY8GqQzby@localhost/sql_test'
db.init_app(app)

class User(db.Model):
   user_id = db.Column(db.Integer, primary_key=True) #readded
   email = db.Column(db.String(120), unique=True)
   fname = db.Column(db.String(80), unique=False)
   age = db.Column(db.Integer, unique=False)
   bio = db.Column(db.String(240), unique=False)
   github = db.Column(db.String(80), unique=False)

   #new
   # tags = db.Column(db.String(240), unique=False)
   # profile_pic = db.Column(db.String(240), unique=False)

   def __repr__(self):
      return '<Task %r>' % self.user_id

# Our match checker, if a user's target id is shared by another user's target id, the pair are matched
class Swipes(db.Model):
   user_id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(120), unique=False)
   target = db.Column(db.Integer, unique=False)

   def __repr__(self):
      return '<Task %r>' % self.user_id

# create a connector
mysql_connector = mysql.connector.connect(host="localhost", 
                                          user="root", 
                                          passwd="lWGTQm32UWinY8GqQzby")

# Create a cursor to access the database from
mycursor = mysql_connector.cursor()

# grab our data base and all of its rows
mycursor.execute("USE sql_test")
mycursor.execute("SELECT * FROM User")

# print the results
for row in mycursor:
   print(row)

#  linkedin_bp = OAuth2ConsumerBlueprint(
#     # DO NOT PUSH TO PROD AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
#     client_id="860v4mkeeipykm",
#     client_secret="dSuEAHyAxPXRqcu4",
#     # DO NOT PUSH TO PROD AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# )

@app.route('/', methods=['POST', 'GET'])
def index():
      return render_template("login.html")

@app.route('/profile', methods=['POST', 'GET'])
def profile():
   tags = ['Python', 'JavaScript', 'React', 'Angular', 'Vue.js', 
                         'Django', 'Flask', 'Node.js', 'Express.js', 'Ruby on Rails', 
                         'PHP', 'Laravel', 'ASP.NET', 'Spring', 'Hibernate', 'jQuery', 
                         'Bootstrap', 'Materialize', 'Sass', 'Less', 'CSS', 'HTML', 
                         'MongoDB', 'MySQL', 'PostgreSQL', 'SQL Server', 'Redis', 
                         'Memcached', 'Apache Kafka', 'RabbitMQ', 'Apache Spark', 
                         'TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn', 'Numpy', 
                         'Pandas', 'Matplotlib', 'Seaborn', 'Data Analysis', 
                         'Data Visualization', 'Machine Learning', 'Artificial Intelligence', 
                         'Deep Learning', 'Computer Vision', 'Natural Language Processing', 
                         'Front End Development', 'Back End Development', 'Full Stack Development', 'DevOps', 'Rust']
   tags.sort()


   if request.method == 'POST':
      user = User.query.filter_by(email=request.form['email']).first()

      if user is None:
         print("User not found, creating! (sourced from profile)")
         fname, age, bio, github = request.form['fname'], request.form['age'], request.form['bio'], request.form['github']
         print(request.form['fname'])
         print(request.form['age'])
         if fname == "":
            fname = "N/A"
         if age == None:
            age = 0
         if bio == None:
            bio = "N/A"
         if github == None:
            github = "N/A"

         
         user = User(email=request.form['email'], fname=fname, age=age, bio=bio, github=github)
         try:
            db.session.add(user)
            db.session.commit()  # update the user in the database
            return redirect('/')
         except Exception as e:
            printError(e)
      else:
         print("User found, updating! (sourced from profile)")
         if request.form['fname'] != "":
            user.fname = request.form['fname']

         if request.form['age'] != "":
            user.age = request.form['age']

         if request.form['bio'] != "":
            user.bio = request.form['bio']

         if request.form['github'] != "":
            user.github = request.form['github']

         try:
            db.session.commit()  # update the user in the database
            return redirect('/')
         except Exception as e:
            printError(e)
   else:
        profile = {'email': 'E-Mail', 'fname': 'Name', 'age': 'Age', 'bio': 'Bio', 'github': 'GitHub Username', 'tags': ['tag1', 'tag2', 'tag3']}
        return render_template("profile.html", profile=profile, tags=tags)

@app.route('/matches', methods=['GET'])
def matches():
   profile = User.query.first()
   return render_template("matches.html", profile=profile)
   
@app.route('/swipe', methods=['POST', 'GET'])
def swipe():

   target = User.query.first()
   matched = Swipes(profile.user_id)
   if request.method == 'POST':
      user = User.query.first() # TODO: replace with current user

   #    if user is None:
   #       print("User not found, creating! (sourced from swipe)")
   #       user = User(email=request.form['email'], fname=request.form['fname'], age=request.form['age'], bio=request.form['bio'], github=request.form['github'])
   #       try:
   #          db.session.add(user)
   #          db.session.commit()  # update the user in the database
   #          return redirect('/')
   #       except Exception as e:
   #          printError(e)
   #    else:
   #       print("User found, updating! (sourced from swipe)")
   #       user.fname = request.form['fname']
   #       user.age = request.form['age']
   #       user.bio = request.form['bio']
   #       user.github = request.form['github']

   #       try:
   #          db.session.update(user)
   #          db.session.commit()  # update the user in the database
   #          return redirect('/profile')
   #       except Exception as e:
   #          printError(e)
   else:
      return render_template("swipe.html", profile=target)

@app.route('/background_process_test')
def background_process_test():
   return("nothing")

def printError(e):
   print("There was an issue saving your profile information to the database... Please try again later. Error message:\n\n\n" + str(e))

def listToString(list):
   return "[ " + ", ".join(list) + "]"

def stringToList(string):
   return string[2:-2].split("', '")

if __name__ == "__main__":
    app.run(debug=True)

