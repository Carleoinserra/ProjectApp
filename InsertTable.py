import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Arcobaleno1",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Giuseppina", "Via Napoli 5")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
