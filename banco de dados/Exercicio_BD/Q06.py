import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#Consultas e Funções Agregadas. Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
# for clientes in dados:
#     print(clientes)

# b) Calcule o saldo médio dos clientes.
# dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
# for clientes in dados:
#     print(clientes)
# c) Encontre o cliente com o saldo máximo.
# dados = cursor.execute('SELECT * FROM clientes WHERE saldo=(SELECT MAX(saldo) FROM clientes)')
# for clientes in dados:
#     print(clientes)

# # d) Conte quantos clientes têm saldo acima de 1000.
# dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000 ')
# for clientes in dados:
#     print(clientes)



#ver os dados 
# dados = cursor.execute('SELECT * FROM clientes')
# for clientes in dados:
#     print(clientes)

conexao.commit()
conexao.close