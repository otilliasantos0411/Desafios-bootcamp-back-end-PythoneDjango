import sqlite3

conexao = sqlite3.connect('python')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios (id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR (100));')

#cursor.execute('CREATE TABLE gerente (id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR (100));')

#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')

#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#cursor.execute('DROP TABLE produtos')

#cursor.execute('ALTER TABLE usuario DROP COLUMN COUMN')


# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (1, "Otilia Santos", "Sao jose", "otylyasousa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (2, "Santos", "Sao jose", "otylyasousa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (3, "ALmira Santos", "Sao jose", "otylyasousa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (4, "Alzira Santos", "Sao jose", "otylyasousa@gmail.com", 123456)')


# cursor.execute('INSERT INTO gerente (id, nome, endereco, email) VALUES (1, "Maria", "peixe", "franca@gmail.com")')

# cursor.execute('INSERT INTO gerente (id, nome, endereco, email) VALUES (2, "jose", "franca", "franca@gmail.com")')
# cursor.execute('DELETE FROM usuario where id=2') """ A operação DELETE é usada para remover registros de uma tabela com base em uma condição específica. """

""" As consultas SELECT são usadas para buscar informações específicas. """
# dados = cursor.execute('SELECT nome, telefone FROM usuario WHERE id>2')
# for usuario in dados:
#     print(usuario)

# cursor.execute('UPDATE usuario SET endereco="Floriano" WHERE nome= "Otilia Santos"') 
# """ A operação UPDATE é usada para modificar os valores de registros existentes em uma tabela. 
# em ordem alfabética crescente (ASC) 
# em ordem decrescente (DESC)  """
""" A cláusula ORDER BY é usada em consultas SQL para especificar a ordenação dos resultados da consulta. """
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome')
# for usuario in dados:
#     print(usuario)

#LIMIT E DISTINCT
# dados = cursor.execute('SELECT * FROM usuario LIMIT 2')
# for usuario in dados:
#     print(usuario)

# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 2')
# for usuario in dados:
#     print(usuario)


#GROUP BY E HAVING
#o GROUP BY é usado para agrupar registros com base em valores de colunas, enquanto 
# o HAVING é usado para filtrar grupos resultantes com base em condições em funções de agregação
# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')
# for usuario in dados:
#     print(usuario)


#Joins
#JOIN- INER 
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerente ON usuario.id = gerente.id')
# for usuario in dados:
#     print(usuario)


# #LEFT JOIN
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerente ON usuario.id = gerente.id')
# for usuario in dados:
#     print(usuario)

# RIGHT JOIN
# dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerente ON usuario.id = gerente.id')
# for usuario in dados:
#     print(usuario)


# FULL JOIN
# dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerente ON usuario.id = gerente.id')
# for usuario in dados:
#     print(usuario)

#sub-consultas

dados = cursor.execute('SELECT * FROM usuario where nome IN (select nome from gerente)')
for usuario in dados:
    print(usuario)


conexao.commit()
conexao.close