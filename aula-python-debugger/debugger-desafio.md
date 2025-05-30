
# Desafio: Sistema Simples de Gerenciamento de Contas Bancárias

## Enunciado

Crie um sistema que gerencie **contas bancárias** com as seguintes características:

### Classe `Conta`

- Atributos:
  - `titular`: nome do cliente (string)
  - `saldo`: saldo da conta (float), valor inicial padrão 0
- Métodos:
  - `depositar(valor)`: adiciona o valor ao saldo
  - `sacar(valor)`: subtrai o valor do saldo se houver saldo suficiente, caso contrário imprime mensagem de erro
  - `extrato()`: retorna o saldo atual formatado como string, por exemplo: `"Saldo de Alice: R$ 1000.00"`

### Classe `Banco`

- Atributo:
  - Lista de contas (`contas`)
- Métodos:
  - `adicionar_conta(conta)`: adiciona uma nova conta à lista
  - `transferir(de_conta, para_conta, valor)`: realiza transferência de valor entre contas se `de_conta` tiver saldo suficiente, senão imprime mensagem de erro

### Script principal

- Crie pelo menos duas contas com titulares e saldos iniciais.
- Realize operações de depósito, saque e transferência entre as contas.
- Imprima o extrato das contas após as operações.

---

## Código base (exemplo)

```python
class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print(f"Saldo insuficiente para {self.titular}")

    def extrato(self):
        return f"Saldo de {self.titular}: R$ {self.saldo:.2f}"


class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def transferir(self, de_conta, para_conta, valor):
        if de_conta.saldo >= valor:
            de_conta.sacar(valor)
            para_conta.depositar(valor)
        else:
            print(f"Transferência não realizada: saldo insuficiente em {de_conta.titular}")


# --- Script principal ---

banco = Banco()

conta1 = Conta("Alice", 1000)
conta2 = Conta("Bob", 500)

banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)

conta1.depositar(200)
conta2.sacar(100)

banco.transferir(conta1, conta2, 500)

print(conta1.extrato())
print(conta2.extrato())
```

---

## Pontos para usar no Debugger do VSCode

- **Breakpoints**: Defina breakpoints dentro dos métodos `depositar`, `sacar`, `transferir` e `extrato` para pausar a execução nestes momentos importantes.
- **Fluxo entre classes**: Observe como a execução entra e sai dos métodos das classes `Conta` e `Banco`.
- **Painel WATCH**: Adicione as variáveis para monitoramento contínuo, por exemplo:
  - `self.saldo`
  - `valor`
  - `de_conta.saldo`
  - `para_conta.saldo`
- **Call Stack**: Acompanhe a pilha de chamadas para entender a sequência das operações.
- **Testes de casos limites**: Modifique o saldo das contas e valores para tentar sacar ou transferir quantias maiores que o saldo e observe como o programa responde.
- **Step Over e Step Into**: Use os botões ou atalhos do VSCode para avançar na execução linha a linha e entrar dentro das funções para entender o comportamento do código.
- **Uso do Watch**: Adicione expressões complexas, por exemplo, `de_conta.saldo - valor` para acompanhar valores calculados dinamicamente.

---

## Objetivos do desafio

- Compreender o uso da orientação a objetos em Python.
- Aprender a usar o debugger do VSCode para acompanhar o fluxo do programa.
- Praticar o monitoramento de variáveis e expressões com Watch.
- Identificar erros comuns relacionados a saldo insuficiente.
- Desenvolver raciocínio para testar cenários diversos usando ferramentas de depuração.

---