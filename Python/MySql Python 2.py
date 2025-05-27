import mysql.connector
import pickle
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "CS2"
)

cursor = connection.cursor()

orisma = input("Give Orisma:")
sql1 = f"CREATE OR REPLACE VIEW ShowTable AS SELECT * FROM CARS WHERE Brand RLIKE '^{orisma}'"

cursor.execute(sql1)

cursor.execute("SELECT * FROM ShowTable")
rows = cursor.fetchall()
print(rows)

cursor.close()
connection.close()