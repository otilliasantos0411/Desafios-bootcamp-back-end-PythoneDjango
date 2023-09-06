import sqlite3

# conexao = sqlite3.connect('banco')
# cursor = conexao.cursor()

# #ver os dados 
# dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)

#Atualização e Remoção
# a)Atualize a idade de um aluno específico na tabel.
# dados = cursor.execute('UPDATE alunos SET idade=25 WHERE id=1')


# b)Remova um aluno com base em seu ID

# dados = cursor.execute('DELETE FROM alunos WHERE id=5')


# #ver os dados 
# dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)

conexao.commit()
conexao.close