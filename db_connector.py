import mysql.connector

def db_connection():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="130245",
    port="3307",
    database='passwordmanager'
    )

    return mydb