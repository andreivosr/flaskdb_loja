import mysql.connector
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

def get_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="db_loja",
        use_pure=True,
    )

@app.route("/clientes", methods=["GET"])
def buscar_clientes():
    mydb = get_conexao()
    cur = mydb.cursor()
    cur.execute("SELECT cli_codigo, cli_nome, cli_email, cli_criado_em FROM clientes")
    tb_clientes = cur.fetchall()
    clientes = list()

    for cliente in tb_clientes:
        clientes.append(
            {
                'id': cliente[0],
                'nome': cliente[1],
                'email': cliente[2],
            }
        )


    return make_response(
        jsonify(
            dados=clientes,
            mensagem = "lista de clientes.",
        )
    )
@app.route("/clientes", methods=["POST"])
def adicionar_cliente():
    cliente = request.json
    mydb = get_conexao()
    mycursor = mydb.cursor()
    sql = "INSERT INTO clientes (cli_nome, cli_email) VALUES (%s, %s)"
    mycursor.execute(sql, (cliente['nome'], cliente['email']))
    mydb.commit()

    return make_response(
        jsonify(
            mensagem = "Cliente adicionado com sucesso.",
            cliente = cliente
        )
    )

if __name__ == "__main__":
    app.run(debug=True)