import mysql.connector
from flask import Flask, jsonify, make_response

app = Flask(__name__)

def get_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db_loja",
        use_pure=True,
    )



if __name__ == "__main__":
    app.run(debug=True)