import socket
import mysql.connector

# Σύνδεση με τη βάση MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="CS1"
)
cursor = db.cursor()

# Δημιουργία socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen(1)
print("Server is running...")

while True:
    client_socket, addr = server.accept()
    print(f"Connected by {addr}")

    data = client_socket.recv(1024).decode()
    if data:
        try:
            Brand, Model, Year = data.split(",")
            cursor.execute("INSERT INTO CARS (Brand, Model,Year) VALUES (%s, %s,%s)", (Brand.strip(),Model.strip(), int(Year.strip())))
            db.commit()
            client_socket.send("Εισαγωγή επιτυχής".encode())
        except Exception as e:
            client_socket.send(f"Σφάλμα εισαγωγής: {str(e)}".encode())

    client_socket.close() 