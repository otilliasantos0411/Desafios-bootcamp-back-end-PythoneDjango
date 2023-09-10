nome_usuario ='Otilia'

def imprimir_no_log(texto, nivel='info'):
    if nivel.lower() == 'info':
        print(f'Info: {texto}')
    elif nivel.lower() == 'aviso':
        print(f'Aviso: {texto}')
    elif nivel.lower() == 'erro':
        print(f'Erro: {texto}')
    else:
        print('Erro interno - nível desconhecido de mensagem')