import sqlite3

conexao = sqlite3.connect('python')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE usuarios (id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR (100));')

#cursor.execute('CREATE TABLE produtos (id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR (100));')

#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')

#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#cursor.execute('DROP TABLE produtos')

#cursor.execute('ALTER TABLE usuario DROP COLUMN COUMN')


# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (1, "Otilia Santos", "Sao jose", "otylyasousa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (2, "Santos", "Sao jose", "otylyasousa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (3, "ALmira Santos", "Sao jose", "otylyasousa@gmail.com", 123456)')
# cursor.execute('INSERT INTO usuario (id, nome, endereco, email, telefone) VALUES (4, "Alzira Santos", "Sao jose", "otylyasousa@gmail.com", 123456)')

# cursor.execute('DELETE FROM usuario where id=2')

dados = cursor.execute('SELECT * FROM usuario')

for usuario in dados:
    print(usuario)


conexao.commit()
conexao.close