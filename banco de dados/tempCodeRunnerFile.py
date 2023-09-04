import sqlite3

conexao = sqlite3.connect('pyton')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE fornecedor(id INT, nome VARCHAR(100), endereco VARCHAR(250));')

conexao.commit()
conexao.close