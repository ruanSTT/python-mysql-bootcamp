# Exercício 1 – Debug passo a passo
def soma_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total

print(soma_lista([1, 2, 3, 4]))

"""
Defina breakpoint dentro do loop.

Adicione num e total no watch.

Use Step Over para avançar e monitorar os valores.
"""


# Exercício 2 – Debug com funções
def multiplicar(a, b):
    return a * b

def calcular():
    x = 3
    y = 4
    resultado = multiplicar(x, y)
    return resultado

print(calcular())
"""
Coloque breakpoint em resultado = multiplicar(x, y).

Use Step Into para entrar na função multiplicar.

Monitore a, b e resultado no Watch.
"""


# Exercício 3 – Acompanhando expressões
def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado

print(potencia(2, 4))

"""
Coloque breakpoint na linha resultado *= base.

Adicione no Watch as expressões: resultado, base, expoente, resultado * base.

Observe os valores enquanto o loop executa.
"""