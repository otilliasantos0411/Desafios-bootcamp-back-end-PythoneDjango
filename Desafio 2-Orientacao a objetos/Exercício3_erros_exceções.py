#Exercício Erros e Exceções

def calcular_media(valores):
    tamanho = len(valores)  # calcular o tamanho corretamente
    soma = 0.0
    for valor in valores:
        soma += valor
    if tamanho > 0:  # Verifica se a lista não está vazia para evitar divisão por zero
        media = soma / tamanho
        return media
    else:
        return None  # Retorna None se a lista estiver vazia

valores = []
continuar = True

while continuar:
    valor_str = input('Digite um número para entrar (ou "ok" para encerrar): ')
    if valor_str.lower() == 'ok':
        continuar = False
    else:
        try:
            valor = float(valor_str)  # Converte o input para um número float
            valores.append(valor)  # Adiciona o valor à lista
        except ValueError:
            print('Digite um número válido.')

media = calcular_media(valores)

if media is not None:
    print(f'A média dos valores é: {media}')
else:
    print('A lista está vazia, não é possível calcular a média.')
