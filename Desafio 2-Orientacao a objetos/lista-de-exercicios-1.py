# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.modelo} ligou o motor.")

    def desliga(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print(f"{self.modelo} desligou o motor.")

    def acelera(self, quantidade):
        if self.ligado:
            self.velocidade += quantidade
            print(f"{self.modelo} acelerou para {self.velocidade} km/h.")

    def desacelera(self, quantidade):
        if self.ligado:
            self.velocidade -= quantidade
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"{self.modelo} desacelerou para {self.velocidade} km/h.")


# Crie uma instância da classe carro.
meu_carro = Carro(cor="Preta", modelo="Celtinha")

# Faça o carro "andar" utilizando os métodos da sua classe.

meu_carro.liga()
meu_carro.acelera(20)

# Faça o carro "parar" utilizando os métodos da sua classe.

meu_carro.desacelera(10)
meu_carro.desliga()
