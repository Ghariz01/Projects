import mysql.connector
import pickle
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "CS2"
)

cursor = connection.cursor()

year = input("Give Year:")

cursor.execute("DROP VIEW IF EXISTS ShowYear")

sql1 = f"""CREATE VIEW ShowYear AS SELECT Brand,Model,Year FROM CARS WHERE Year = '{year}'"""
cursor.execute(sql1)

sql2 = """Select * from ShowYear"""

cursor.execute(sql2)
rows = cursor.fetchall()
print(rows)

cursor.close()
connection.close()