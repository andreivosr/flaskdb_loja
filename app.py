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
    meubanco = get_conexao()
    cursor = meubanco.cursor() #objeto usado para executar comandos SQL
    cursor.execute("SELECT cli_codigo, cli_nome, cli_email, cli_criado_em FROM clientes")
    tb_clientes = cursor.fetchall()
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
    meubanco = get_conexao()
    cursor = meubanco.cursor()
    sql = "INSERT INTO clientes (cli_nome, cli_email) VALUES (%s, %s)"
    cursor.execute(sql, (cliente['nome'], cliente['email']))
    meubanco.commit()

    return make_response(
        jsonify(
            mensagem = "Cliente adicionado com sucesso.",
            cliente = cliente
        )
    )

@app.route("/clientes/<id>", methods=["DELETE"])
def excluir_cliente(id):
    meubanco = get_conexao()
    cursor = meubanco.cursor()
    sql = "DELETE FROM clientes WHERE cli_codigo = %s"
    cursor.execute(sql, (id,))
    meubanco.commit()
    return make_response(
        jsonify(
            mensagem = "Cliente excluido com sucesso.",
        )
    )

@app.route("/clientes/<int:id>", methods=["PUT"])
def atualizar_cliente(id):
    cliente = request.json
    meubanco = get_conexao()
    cursor = meubanco.cursor()

    sql = "UPDATE clientes SET cli_nome = %s, cli_email = %s WHERE cli_codigo = %s"
    valores = (cliente['nome'], cliente['email'], id)

    cursor.execute(sql, valores)
    meubanco.commit()
    return make_response(
        jsonify(
            mensagem = "Cliente atualizado com sucesso!"
        )
    )

if __name__ == "__main__":
    app.run(debug=True)