# Exercícios:Conceitos Básicos em Python
#Exercicio 1.Faça um Programa que peça um número e entã o mostre a mensagem:-> O
#número informado foi [número].

""" numero =int(input('Digite um número:'))

print(f'O número informado foi {numero}') """

# Exercicio 2: Faça um Programa que peça dois números e imprima a soma.
""" 
numero1 =int(input('Digite um numero 01:'))
numero2 =int(input('Digite um numero 02:'))
soma= numero1+numero2
print(f'A soma dos números é {soma}') """

# Exercicio 3: Faça um Programa que peça a temperatura em graus Celsius,transforme e mostre em graus Fahrenheit.
# Solicita a temperatura em graus Celsius
""" celsius = float(input("Digite a temperatura em graus Celsius: "))

# Faz a conversão de Celsius para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostra o resultado
print(f"{celsius:.2f} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit") """

# Exercicio 4.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.


# Solicita o valor do salário por hora e o número de horas trabalhadas no mês
valor_por_hora = float(input("Digite o valor do salário por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário total
salario_total = valor_por_hora * horas_trabalhadas

# Mostra o resultado
print(f"Seu salário total no mês é: R$ {salario_total:.2f}")
