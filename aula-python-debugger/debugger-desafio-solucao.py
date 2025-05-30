class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print(f"Erro: valor de depósito inválido para {self.titular}")
            return
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado para {self.titular}")

    def sacar(self, valor):
        if valor <= 0:
            print(f"Erro: valor de saque inválido para {self.titular}")
            return
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado para {self.titular}")
        else:
            print(f"Saldo insuficiente para {self.titular}")

    def extrato(self):
        return f"Saldo de {self.titular}: R$ {self.saldo:.2f}"


class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        print(f"Conta adicionada para {conta.titular}")

    def transferir(self, de_conta, para_conta, valor):
        if valor <= 0:
            print("Erro: valor de transferência inválido")
            return
        if de_conta.saldo >= valor:
            de_conta.sacar(valor)
            para_conta.depositar(valor)
            print(f"Transferência de R$ {valor:.2f} de {de_conta.titular} para {para_conta.titular} realizada com sucesso")
        else:
            print(f"Transferência não realizada: saldo insuficiente em {de_conta.titular}")


# --- Script principal ---

banco = Banco()

conta1 = Conta("Alice", 1000)
conta2 = Conta("Bob", 500)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

conta1.depositar(200)     # Alice agora tem 1200
conta2.sacar(100)         # Bob agora tem 400

banco.transferir(conta1, conta2, 500)  # Alice 700, Bob 900

print(conta1.extrato())
print(conta2.extrato())