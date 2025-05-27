from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout , QTableWidget, QTableWidgetItem
import sys
import mysql.connector

connection = mysql.connector.connect(
host ="localhost",
user ="root",
database ="DB1"
)

cursor = connection.cursor()

# Δημιουργία εφαρμογής
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Insert Cars")
window.setGeometry(500, 300, 1000, 500)

# Ετικέτα
label = QLabel("Πληκτρολογήστε κάτι😊")

# Textbox
textbox_brand = QLineEdit()
textbox_brand.setPlaceholderText("Brand...")
textbox_model = QLineEdit()
textbox_model.setPlaceholderText("Model...")
textbox_year = QLineEdit()
textbox_year.setPlaceholderText("Year...")

# Πίνακας για την εμφάνιση των δεδομένων
table = QTableWidget()
table.setColumnCount(7)
table.setHorizontalHeaderLabels(["ID_Car","Brand", "Model", "Year","ID_T", "Max Speed", "Kilometers"])

# Κουμπί
button = QPushButton("Υποβολή")

# Συνάρτηση που εκτελείται όταν πατηθεί το κουμπί
def on_button_click():
    brand = textbox_brand.text()
    model = textbox_model.text()
    year = textbox_year.text()
    sql = """
          SELECT Cars.ID_Car,Cars.Brand,Cars.Model,Cars.Year,Technical.ID_Tech,Technical.MaxSpeed,Technical.Kilometers
          FROM Technical JOIN Cars ON Technical.ID_Tech = Cars.Technical_ID_Tech
          WHERE Cars.Brand = %s OR Cars.Model = %s OR Cars.Year = %s 
          """

    cursor.execute(sql, (brand, model, year))
    rows = cursor.fetchall()
    table.setRowCount(len(rows))

    for row_number, row_data in enumerate(rows):
        for column_number, data in enumerate(row_data):
            table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

button.clicked.connect(on_button_click)

# Διάταξη
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(table)
layout.addWidget(textbox_brand)
layout.addWidget(textbox_model)
layout.addWidget(textbox_year)
layout.addWidget(button)
window.setLayout(layout)

# Προβολή παραθύρου
window.show
()
sys.exit(app.exec_())

cursor.close()
connection.close() 