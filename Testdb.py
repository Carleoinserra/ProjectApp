import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Test1234"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")