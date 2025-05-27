import socket

# Λήψη δεδομένων από τον χρήστη
Brand = input("Brand: ")
Model = input("Model: ")
Year = input("Year: ")

# Σύνδεση με τον server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))

# Αποστολή δεδομένων
client.send(f"{Brand},{Model},{Year}".encode())

# Λήψη απάντησης
response = client.recv(1024).decode()
print("Απάντηση server:", response)

client.close() 