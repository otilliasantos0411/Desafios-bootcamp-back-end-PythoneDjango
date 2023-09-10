from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

    @abstractmethod
    def tem_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.cheque_especial = renda_mensal

    def tem_cheque_especial(self):
        return True

class ClienteHomem(Cliente):
    def tem_cheque_especial(self):
        return False

class ContaCorrente:
    def __init__(self, clientes):
        self.clientes = clientes
        self.saldo = 0
        self.operacoes = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f"Depósito de R${valor:.2f}")

    def saque(self, valor):
        if valor > 0:
            if self.tem_saldo_suficiente(valor):
                self.saldo -= valor
                self.operacoes.append(f"Saque de R${valor:.2f}")
            else:
                self.operacoes.append("Saque negado (saldo insuficiente)")

    def tem_saldo_suficiente(self, valor):
        saldo_total = self.saldo
        for cliente in self.clientes:
            if isinstance(cliente, ClienteMulher):
                saldo_total += cliente.cheque_especial
        return saldo_total >= valor

# Exemplo de uso:

# Criando clientes
cliente_mulher = ClienteMulher("Maria", "123-456-7890", 3000)
cliente_homem = ClienteHomem("João", "987-654-3210", 2500)

# Criando uma conta corrente com os clientes
conta = ContaCorrente([cliente_mulher, cliente_homem])

# Realizando operações
conta.deposito(1000)
conta.saque(2000)
conta.saque(4000)

# Exibindo o saldo e as operações
print(f"Saldo da conta: R${conta.saldo:.2f}")
print("Operações:")
for operacao in conta.operacoes:
    print(operacao)
