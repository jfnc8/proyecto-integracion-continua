from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "root123"),
        database=os.getenv("DB_NAME", "mi_base")
    )

@app.route("/")
def inicio():
    return "<h1>Proyecto Integracion Continua</h1><p>App funcionando con Flask y MySQL</p><p><a href='/usuarios'>Ver usuarios</a></p>"

@app.route("/usuarios")
def usuarios():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        datos = cursor.fetchall()
        conn.close()
        return jsonify(datos)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/salud")
def salud():
    return jsonify({"estado": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
