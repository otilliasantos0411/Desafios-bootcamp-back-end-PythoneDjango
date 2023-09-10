""" lista = [] #Uma lista é uma sequência ordenada e mutável de valores, que podem ser de tipos diferentes.
fruta = input('Digite sua fruta:')
lista.append(fruta)
print(lista)

#tuplas: Uma tupla é uma sequência ordenada e imutável de valores, que podem ser de tipos diferentes.
#rtuplas sao listas que nao podem ter valores alterados

tupla = ('maca', 'Banana')
print(tupla) """

# dicionario 
#dicionario = {'chave':'valor'} 
""" dicionario['maca'] = 'é uma fruta'
dicionario['carro'] = 'é um veiculo'
dicionario['Gato'] = 'é um animal'
print(dicionario)
 """
#Exercícios:Listas,Tuplas e Dicionários
# 1."Faça um Programaquepeçaasquatronotasde10alunos,calculeearmazenenumalistaamédiadecadaaluno,imprimaonúmerodealunoscommédiamaiorouiguala7.0.

# Cria uma lista vazia para armazenar as médias dos alunos
""" medias_alunos = []

# Loop para pedir as notas de 10 alunos
for i in range(10):
    print(f"Aluno {i+1}:")
    notas = []
    for j in range(4):
        nota = float(input(f"Informe a nota {j+1}: "))
        notas.append(nota)
    
    # Calcula a média das notas do aluno
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

# Conta e imprime o número de alunos com média maior ou igual a 7.0
count = 0
for media in medias_alunos:
    if media >= 7.0:
        count += 1

print(f"Número de alunos com média maior ou igual a 7.0: {count}")
 """
# 2. Programanomeaocontrárioemmaiúsculas.Façaumprogramaquepermitaaousuáriodigitaroseunomeeemseguidamostreonomedousuáriodetrásparafrenteutilizandosomenteletrasmaiúsculas.Dica:lembre−sequeaoinformaronomeousuáriopodedigitarletrasmaiúsculasouminúsculas
""" nome = input("Digite o seu nome: ")
nome_reverso = nome[::-1].upper()
print("Nome ao contrário em maiúsculas:", nome_reverso)
 """

#3. Escreva um programa em Python que onde 
# todos os valores em um dicionário são emitidos.
# Se sim,imprima True. Caso contrário,imprima Falso
""" 
dicionario = {'banana':'fruta','casa':'imovel','laranja':'fruta' } 

valores_emitidos = all(valor for valor in dicionario.values())

if valores_emitidos:
    print("True")
else:
    print("False") """

#4."Utilizandolistasfaçaumprogramaquefaça5perguntasparaumapessoasobreumcrime.

""" perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas_positivas = 0

for pergunta in perguntas:
    resposta = input(pergunta + " (sim/não): ")
    if resposta.lower() == "sim":
        respostas_positivas += 1

if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")
 """