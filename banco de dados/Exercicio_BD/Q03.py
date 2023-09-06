import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

""" ConsultasBásicasEscrevaconsultasSQLpararealizarasseguintestarefas: """
# a)Selecionartodososregistrosdatabela"alunos".
# cursor.execute('SELECT * FROM alunos')

# dados = cursor.execute('SELECT * FROM alunos')
# for alunos in dados:
#     print(alunos)

# b)Selecionaronomeeaidadedosalunoscommaisde20anos.

# dados = cursor.execute('SELECT * FROM alunos WHERE idade>20')
# for alunos in dados:
#     print(alunos)

# c)Selecionarosalunosdocursode"Engenharia"emordemalfabética.
# dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
# for alunos in dados:
#     print(alunos)

# d)Contaronúmerototaldealunosnatabela
# dados = cursor.execute('SELECT  COUNT (*) FROM alunos')
# for alunos in dados:
#     print(alunos)


conexao.commit()
conexao.close