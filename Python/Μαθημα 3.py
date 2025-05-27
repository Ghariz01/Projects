import socket
import mysql.connector

# Σύνδεση με τη βάση MySQL
def conn():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="DB1")
    return connection

def cursor(connection):
    cursor = connection.cursor()
    return cursor

# Δημιουργία socket server
def sock():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 60000))
    server.listen(1)
    print("Server is running...")
    client_socket, addr = server.accept()
    print(f"Connected by {addr}")
    return client_socket

def client(client_socket):
    data = client_socket.recv(1024).decode()
    Brand, Model, Year, MaxSpeed, Kilometers = data.split(",")
    return Brand, Model, Year, MaxSpeed, Kilometers

def insert(Brand, Model, Year, MaxSpeed, Kilometers,client_socket,connection,cursor):
    try:
        cursor.execute("INSERT INTO Cars (Brand, Model,Year) VALUES (%s, %s,%s)",
                       (Brand.strip(), Model.strip(), int(Year.strip())))
        connection.commit()
        cursor.execute("INSERT INTO Technical (MaxSpeed,Kilometers) VALUES (%s, %s)",
                       (int(MaxSpeed.strip()), int(Kilometers.strip())))
        connection.commit()
        client_socket.send("Εισαγωγή επιτυχής".encode())
    except Exception as e:
        client_socket.send(f"Σφάλμα εισαγωγής: {str(e)}".encode())

while True:
    connection = conn()
    cursor = cursor(connection)
    client_socket = sock()
    Brand, Model, Year, MaxSpeed, Kilometers= client(client_socket)
    insert(Brand, Model, Year, MaxSpeed, Kilometers,client_socket,connection,cursor)

    client_socket.close()