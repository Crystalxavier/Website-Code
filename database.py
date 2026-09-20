import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="rewear_user",
        password="ReWear@123",
        database="rewear_db"
    )

    return connection