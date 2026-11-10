
from flask import Flask, jsonify, render_template
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root123"),
        database=os.getenv("DB_NAME", "mi_base"),
        connection_timeout=5
    )

def estado_db():
    conn = None
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        cursor.close()
        return True
    except mysql.connector.Error:
        return False
    finally:
        if conn is not None and conn.is_connected():
            conn.close()

@app.route("/")
@app.route("/salud")
def inicio():
    return render_template("index.html")

@app.route("/api/salud")
def salud():
    conectado = estado_db()
    return jsonify({
        "estado": "ok",
        "servidor": "Flask operativo",
        "mysql": "conectado" if conectado else "desconectado"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

