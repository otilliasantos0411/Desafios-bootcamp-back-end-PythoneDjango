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

# Criando uma instância da classe Carro
meu_carro = Carro(cor="Vermelho", modelo="Ferrari")

# Ligando o carro
meu_carro.liga()

# Acelerando o carro
meu_carro.acelera(50)

# Desacelerando o carro
meu_carro.desacelera(20)

# Parando o carro
meu_carro.desliga()
