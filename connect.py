import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_loja",
    use_pure=True,
)

cur = mydb.cursor()
cur.execute("SELECT cli_nome, cli_email FROM clientes")
for linha in cur.fetchall():
    print(linha)

mydb.close()