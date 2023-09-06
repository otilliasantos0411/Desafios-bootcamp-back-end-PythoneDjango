dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerente ON usuario.id = gerente.id')
for usuario in dados:
    print(usuario)