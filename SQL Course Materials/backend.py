import mysql.connector

# connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="lWGTQm32UWinY8GqQzby",
  database='sql_store'
)

# create a cursor
mycursor = mydb.cursor()

# execute a query
mycursor.execute("SELECT * FROM customers")

# fetch the results
results = mycursor.fetchall()

# print the results
for row in results:
  print(row)
