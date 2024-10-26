import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="123456",
  database="isbn_db"
)

cursor = mydb.cursor()

cursor.execute("DROP TABLE IF EXISTS task")

sql ='''CREATE TABLE task (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
)'''

cursor.execute(sql)
mydb.close()
