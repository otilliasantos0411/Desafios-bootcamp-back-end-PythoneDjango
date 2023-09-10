from funcoes_do_log import nome_usuario, imprimir_no_log

imprimir_no_log(f'Bem vinda, {nome_usuario}!')

# O primeiro datetime é o nome do módulo, o segundo é o nome de uma classe que existe dentro
# desse módulo
from datetime import datetime
agora = datetime.now()
print(agora)