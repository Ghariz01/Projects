from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
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
window.setGeometry(500, 300, 600, 200)

# Ετικέτα
label = QLabel("Car Deletion")
label2= QLabel("Number of records deleted")

# Textbox
textbox_brand = QLineEdit()
textbox_brand.setPlaceholderText("Brand...")
textbox_model = QLineEdit()
textbox_model.setPlaceholderText("Model...")
textbox_year = QLineEdit()
textbox_year.setPlaceholderText("Year...")

# Κουμπί
button = QPushButton("DELETE CAR")

# Συνάρτηση που εκτελείται όταν πατηθεί το κουμπί
def on_button_click():
    brand = textbox_brand.text()
    model = textbox_model.text()
    year = textbox_year.text()

    if brand and model and year:
        try:
            cursor.execute(
                "SELECT Technical_ID_Tech FROM Cars WHERE Brand=%s AND Model=%s AND Year=%s",
                (brand, model, year)
            )
            result = cursor.fetchone()

            if result:
                tech_id = result[0]
                cursor.execute(
                    "DELETE FROM Cars WHERE Brand=%s AND Model=%s AND Year=%s",
                    (brand, model, year)
                )
                deleted_rows = cursor.rowcount
                connection.commit()
                cursor.execute(
                    "SELECT COUNT(*) FROM Cars WHERE Technical_ID_Tech=%s",
                    (tech_id,)
                )
                count_result = cursor.fetchone()
                if count_result[0] == 0:
                    cursor.execute(
                        "DELETE FROM Technical WHERE ID_Tech=%s",
                        (tech_id,)
                    )
                    connection.commit()

                label.setText(f"The car: {brand} {model} of Year:{year} deleted from the database")
                label2.setText(f"Record(s) deleted: {deleted_rows}")
            else:
                label.setText("No matching car found.")

        except Exception as e:
            label.setText("Car Deletion Failed")
            label2.setText(str(e))
        finally:
            textbox_brand.clear()
            textbox_model.clear()
            textbox_year.clear()
    else:
        label.setText("Fill all the 3 fields!!!!")

button.clicked.connect(on_button_click)

# Διάταξη
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(label2)
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