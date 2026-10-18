
import os
import time
from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_db_connection():
    
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "simpleapp")
    )

@app.route("/")
def home():
    return """
        <h1>Simple App</h1>
        <p>Aplikasi Flask berhasil berjalan.</p>
        <p><a href="/db-check">Periksa koneksi database</a></p>
    """

@app.route("/db-check")
def db_check():
    connection = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE(), VERSION()")
        result = cursor.fetchone()
        cursor.close()

        return f"""
            <h1>Koneksi Database Berhasil!</h1>
            <p>Database: {result[0]}</p>
            <p>Versi MySQL: {result[1]}</p>
        """
    except Error as e:
        return f"<h1>Koneksi database gagal</h1><p>{e}</p>", 500
    finally:
        if connection and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
