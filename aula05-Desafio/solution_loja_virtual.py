"""
solution_loja_virtual.py
-----------------------
Resolução de referência para o super‑desafio final.

• Define as classes Produto, Cliente e Pedido (com herança).
• Demonstra a criação de um pedido, cálculo do total e gravação no banco.
• Inclui um bloco de testes unitários usando unittest.

OBS.: 
- Ajuste as credenciais do banco (host, user, password, database).
- A tabela `pedidos` deve existir no SGBD escolhido.
"""

from typing import List
from decimal import Decimal
import pymysql
import unittest


class Produto:
    """Representa um produto da loja."""

    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = float(preco)

    def exibir_produto(self) -> str:
        return f"{self.nome} - R$ {self.preco:.2f}"


class Cliente:
    """Representa um cliente."""

    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email


class Pedido(Cliente):
    """Pedido herda de Cliente e agrega produtos."""

    def __init__(self, nome: str, email: str):
        super().__init__(nome, email)
        self.itens: List[Produto] = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.itens.append(produto)

    def total_pedido(self) -> float:
        return float(sum(item.preco for item in self.itens))

    def salvar_no_banco(self) -> None:
        """Persistência simples usando PyMySQL."""
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='SENHA',       # <- alterar a senha para a senha do banco
            database='loja_virtual2',
            autocommit=True
        )
        with conexao.cursor() as cur:
            sql = (
                "INSERT INTO pedidos (cliente_nome, cliente_email, total) "
                "VALUES (%s, %s, %s)"
            )
            cur.execute(
                sql,
                (self.nome, self.email, Decimal(str(self.total_pedido())))
            )
        conexao.close()


# ----------------------
# Bloco de demonstração
# ----------------------
def main_demo():
    camisa = Produto("Camisa", 50.0)
    calca = Produto("Calça", 100.0)

    pedido = Pedido("João", "joao@email.com")
    pedido.adicionar_produto(camisa)
    pedido.adicionar_produto(calca)

    print("Total do pedido:", pedido.total_pedido())
    # Descomente para salvar (requer tabela no banco)
    # pedido.salvar_no_banco()


# ---------------------------
# Testes unitários de exemplo
# ---------------------------
class TestPedido(unittest.TestCase):
    def test_total_pedido(self):
        p1 = Produto("Produto 1", 30.0)
        p2 = Produto("Produto 2", 20.0)
        pedido = Pedido("Maria", "maria@email.com")
        pedido.adicionar_produto(p1)
        pedido.adicionar_produto(p2)
        self.assertEqual(pedido.total_pedido(), 50.0)


if __name__ == "__main__":
    # Executa demonstração e testes
    main_demo()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
