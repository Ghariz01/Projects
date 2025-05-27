import mysql.connector
import pickle
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "CS2"
)

cursor = connection.cursor()

sql1 = """GRANT SELECT , INSERT ON *.* TO 'root'@'localhost"""
cursor.execute(sql1)

brand = input("Give Brand:")
model = input("Give Model:")
year = input("Give Model")

sql2 = f"INSERT INTO CARS (Brand , Model , Year) VALUES ('{brand}','{model}','{year}')"

sql = """SELECT * FROM CARS"""

try:
    cursor.execute(sql2)
    connection.commit()
except:
    print("Insert Failed")
else:
    print("Insert Ok")
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows)
    try:
        with open("cars2.pkl","wb") as f:
            pickle.dump(rows,f)
    except:
        print("Error In Saving")
    else:
        print("Data Saved")

sql3 = """ALTER TABLE CARS MODIFY COLUMN YEAR INT"""
cursor.execute(sql3)
connection.commit()

cursor.close()
connection.close()