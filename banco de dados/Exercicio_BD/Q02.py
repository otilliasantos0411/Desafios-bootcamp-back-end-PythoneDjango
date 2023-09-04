import sqlite3

conexao = sqlite3.connect('teste.db')
cursor = conexao.cursor()

# Insere 5 registros de alunos na tabela
alunos = [
    (1, 'João', 20, 'Engenharia'),
    (2, 'Maria', 22, 'Medicina'),
    (3, 'Carlos', 19, 'Direito'),
    (4, 'Ana', 21, 'Ciência da Computação'),
    (5, 'Pedro', 18, 'Administração')
]

# Use uma instrução SQL de inserção para adicionar os registros
cursor.executemany('INSERT INTO alunos (id, nome, idade, curso) VALUES (?, ?, ?, ?)', alunos)

# Salva as alterações e fecha a conexão com o banco de dados
conexao.commit()
conexao.close