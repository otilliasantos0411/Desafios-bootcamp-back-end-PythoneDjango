import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#Criar uma Tabela e Inserir Dados. 
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float).
#  Insira alguns registros de clientes na tabela.

# Cria a tabela "clientes"
# cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY,  nome VARCHAR(100), idade INT, saldo REAL)')


#  Insira alguns registros de clientes na tabela.

#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "João", 30, 1000.0)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES  (2, "Maria", 25, 1500.5)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES  (3, "Carlos", 28, 800.75)')
cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES  (4, "Ana", 35, 2000.25)')


#ver os dados 
dados = cursor.execute('SELECT * FROM clientes')
for clientes in dados:
    print(clientes)

conexao.commit()
conexao.close