from flask import Flask
import os
import pymysql

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "ejemplo"),
        password="SuperPassword123",
        database=os.getenv("DB_NAME", "ejemplo"),
        connect_timeout=5
    )


@app.route("/")
def home():
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        return {
            "status": "ok",
            "message": "API DevSecOps funcionando",
            "database": "connected"
        }, 200

    finally:
        connection.close()


@app.route("/health")
def health():
    connection = get_db_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        return {
            "status": "healthy",
            "database": "connected"
        }, 200

    finally:
        connection.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
