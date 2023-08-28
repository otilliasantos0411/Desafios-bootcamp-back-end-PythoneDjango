#Exercícios:Funções
#1.Façaumprograma,comumafunçãoquenecessitedetrêsargumentos,equeforneçaasomadessestrêsargumentos.

""" def somar_tres_numeros(a, b, c):
    soma = a + b + c
    return soma
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

resultado = somar_tres_numeros(numero1, numero2, numero3)

print("A soma dos três números é:", resultado) """

#2."Reversodonúmero.Façaumafunçãoqueretorneoreversodeumnúmerointeiroinformado.Porexemplo:127->721.

""" def reverso_numero(numero):
    reverso = 0
    while numero > 0:
        digito = numero % 10
        reverso = reverso * 10 + digito
        numero = numero // 10
    return reverso

numero_original = int(input("Digite um número inteiro: "))

numero_reverso = reverso_numero(numero_original)

print("O reverso do número é:", numero_reverso) """

#3.EscrevaumscriptqueperguntaaousuárioseeledesejaconverterumatemperaturadegrauCelsiusparaFahrenheitouvice-versa.
#Paracadaopção,crieumafunção.Crieumaterceira,queéummenuparaousuárioescolheraopçãodesejada,ondeessemenuchamaafunçãodeconversãocorreta.

""" def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    print("Escolha a conversão:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    
    opcao = int(input("Digite o número da opção desejada: "))
    
    if opcao == 1:
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
    else:
        print("Opção inválida!")

# Chama a função de menu
menu()
 """