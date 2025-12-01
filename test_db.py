import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="minibank",
        port=3306
    )
    print("Connected:", db)
except Exception as e:
    print("Error:", e)
