import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Insere 5 registros de alunos na tabela
alunos = [
    (1, 'João', 20, 'Engenharia'),
    (2, 'Maria', 22, 'Medicina'),
    (3, 'Carlos', 19, 'Direito'),
    (4, 'Ana', 21, 'Ciência da Computação'),
    (5, 'Pedro', 18, 'Administração')
]

# Instrução SQL de inserção para adicionar os registros
cursor.executemany('INSERT INTO alunos (id, nome, idade, curso) VALUES (?, ?, ?, ?)', alunos)
 #ou
 #cursor.execute('INSERT INTO alunos (id, nome, idade, curso) VALUES (6, "Otilia", "SIstemas de INformacao")')

conexao.commit()
conexao.close