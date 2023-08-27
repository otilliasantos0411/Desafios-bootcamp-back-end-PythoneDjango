
#operadores relacionais

""" ==	Igual a
!=	Diferente
>=	Maior ou igual
>	Maior que
<	Menor que
<=	Maior ou igual
 """

#Exercícios:Tomada de Decisão e Estruturas de Repetição
# 1.Faça um Programa que peça dois números e imprima o maior deles.

""" numero1 =int(input('Digite um numero 01:'))
numero2 =int(input('Digite um numero 02:'))

if numero1 > numero2:
    maiornumero = numero1
else:
    maiornumero = numero2

print(f"O maior número é: {maiornumero}") """

#2.Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. 
# Imprima a mensagem "Bom Dia!","Boa Tarde!"ou"Boa Noite!"ou"Valor Inválido!",
# conforme o caso.

""" turno = input("Em qual turno você estuda? (M-matutino, V-vespertino, N-noturno): ")

turno = turno.upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:4
    print("Valor Inválido!") """

#3.Faça um programa que peça uma nota,entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

""" while True:
    nota = float(input("Digite uma nota entre 0 e 10:"))
    if 0<= nota <=10:
        break
    else:
        print ("valor invalido {nota:.2f}. Digite novamente:")

print(f"Você inseriu a nota {nota:.2f}, valor válido.") """