#Exercícios: Extras de Python
#Crieumprogramaqueleiaquantodinheiroumapessoatemnacarteira,ecalculequantopoderiacomprardecadamoedaestrangeira.

""" dinheiro = float(input("Digite a quantidade de dinheiro na carteira (em reais): "))

conversoes = {
    "Dólar Americano": 4.91,
    "Peso Argentino": 0.02,
    "Dólar Australiano": 3.18,
    "Dólar Canadense": 3.64,
    "Franco Suíço": 0.42,
    "Euro": 5.36,
    "Libra Esterlina": 6.21
}

print("\nQuantidade que poderia comprar de cada moeda estrangeira:")
for moeda, taxa in conversoes.items():
    quantidade = dinheiro / taxa
    print(f"{moeda}: {quantidade:.2f}")
 """
#2. Escrevaumprogramaquepergunteaquantidadedekmpercorridosporum
# carroalugadoeaquantidadedediaspelosquaiselefoialugado.Calculeopreçoapagar,sabendoqueocarrocustaR$80,00pordiaeR$0,20porkmrodado.
""" km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_aluguel = int(input("Digite a quantidade de dias de aluguel: "))

preco_por_dia = 80.00
preco_por_km = 0.20

preco_total = (preco_por_dia * dias_aluguel) + (preco_por_km * km_percorridos)

print("O preço total a pagar é: R$", preco_total) """

#3.Façaumalgoritmoqueleiaosaláriodeumfuncionárioemostreseunovosalário.
""" 
salario = float(input("Digite o salário do funcionário: "))

if salario <= 1000.00:
    novo_salario = salario * 1.20  # 20% de aumento
elif salario <= 2800.00:
    novo_salario = salario * 1.10  # 10% de aumento
else:
    novo_salario = salario * 1.05  # 5% de aumento

print("Novo salário: R$", novo_salario) """

#4. CrieumprogramaquetenhaafunçãoleiaInt(),quevaifuncionardeformasemelhanteàfunçãoinput()doPython,
# sóquefazendoavalidaçãoparaaceitarapenasumvalornúmerico

while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break  # Sai do loop se um valor válido for inserido
    except ValueError:
        print("Erro: Digite um valor numérico válido.")

print(f"Você digitou: {numero}")