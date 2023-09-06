import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), 
# cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
# Insira algumas compras associadas a clientes existentes na tabela "clientes". 
# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

# Criação da tabela "compras"
# cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY, cliente_id INTEGER, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')


# cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES  (1, "Produto A", 100.00)')
# cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES  (2, "Produto B", 50.00)')
# cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES  (1, "Produto C", 75.50)')
# cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES  (3, "Produto D", 120.00)')
# cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES  (2, "Produto E", 80.25)')

dados = cursor.execute('SELECT nome, produto, valor FROM clientes JOIN compras ON clientes.id = compras.id')
for clientes in dados:
    print(clientes)

# # #ver os dados 
# dados = cursor.execute('SELECT * FROM compras')
# for compras in dados:
#     print(compras)

conexao.commit()
conexao.close