import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Cria a tabela "alunos"
cursor.execute('CREATE TABLE alunos (id INTEGER PRIMARY KEY, nome VARCHAR(100), idade INT, curso VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos (id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR (100));')

# Salva as alterações e fecha a conexão com o banco de dados
conexao.commit()
conexao.close