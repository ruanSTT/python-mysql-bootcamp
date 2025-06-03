# 📝 Exercícios — Integração Python e Banco de Dados (02/06/2025)

## 💾 Tema: Consultas e Inserções em SQL (Banco: loja_virtual)

---

### 🧪 Exercício 1 — Inserindo novos produtos

**Objetivo**: Inserir dois novos produtos na tabela `produtos`, usando comandos SQL, respeitando o mesmo padrão dos dados já existentes.

#### 🔧 Enunciado

Adicione à tabela `produtos` os seguintes itens:

| nome               | preco   | estoque |
|--------------------|---------|---------|
| Headset Bluetooth  | 199.99  | 25      |
| Webcam Full HD     | 249.90  | 40      |

#### ✅ Solução esperada

```sql
INSERT INTO produtos (nome, preco, estoque) VALUES
  ('Headset Bluetooth', 199.99, 25),
  ('Webcam Full HD', 249.90, 40);
```

---

### 🧪 Exercício 2 — Realizando consultas específicas

**Objetivo**: Escrever consultas SQL para extrair informações específicas da tabela `produtos`.

#### 🔧 Enunciado

Com base nos dados da tabela `produtos`, crie os comandos SQL para responder:

**a)** Quais produtos custam mais de R$300?  
**b)** Quais produtos têm menos de 20 unidades no estoque?

#### ✅ Solução esperada

```sql
-- a) Produtos com preço acima de R$300
SELECT * FROM produtos WHERE preco > 300;

-- b) Produtos com menos de 20 unidades em estoque
SELECT * FROM produtos WHERE estoque < 20;
```

---

### 📚 Dicas extras

- Para ordenar os resultados por preço (decrescente):
```sql
SELECT * FROM produtos ORDER BY preco DESC;
```

- Para retornar apenas nome e preço:
```sql
SELECT nome, preco FROM produtos;
```

---

🧠 **Desafio extra (opcional)**:  
Liste todos os produtos cujo nome contém a palavra `"HD"`.

```sql
SELECT * FROM produtos WHERE nome LIKE '%HD%';
```