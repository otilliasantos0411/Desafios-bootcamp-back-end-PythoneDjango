import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# Atualização e Remoção com Condições. 
# a) Atualize o saldo de um cliente específico. 
# dados = cursor.execute('UPDATE clientes SET saldo=2000 WHERE id=1')

# b) Remova um cliente pelo seu ID.

# dados = cursor.execute('DELETE FROM clientes WHERE id=4')



# #ver os dados 
# dados = cursor.execute('SELECT * FROM clientes')
# for clientes in dados:
#     print(clientes)

conexao.commit()
conexao.close