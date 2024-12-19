# 🧬 Carga Evolutiva: Otimização de Carga com Algoritmo Genético

Este projeto implementa um **algoritmo genético** sem bibliotecas externas para resolver um problema de otimização de carga em transporte. Ele busca encontrar a melhor combinação de produtos para transportar, respeitando um limite de espaço e maximizando o valor total da carga.

## 📌 Descrição

O projeto utiliza uma população de indivíduos (soluções candidatas), onde cada indivíduo representa uma combinação de produtos a serem transportados. O algoritmo evolui através de várias gerações, aplicando os seguintes passos:

1. **Avaliação** da aptidão (fitness) de cada indivíduo com base no valor total e no espaço ocupado.
2. **Seleção** dos melhores indivíduos para reprodução.
3. **Cruzamento (Crossover)** para gerar novos indivíduos.
4. **Mutação** para manter a diversidade da população.

O objetivo é encontrar a combinação de produtos que maximize o valor total transportado sem exceder o limite de espaço.

---

## 🚀 Execução do Projeto

### **1. Pré-requisitos**

- **Python 3.x** instalado.
- Servidor **MySQL** configurado com uma base de dados `produtos`.
- Biblioteca `mysql-connector-python` instalada.

Para instalar a biblioteca:

```bash
pip install mysql-connector-python
```

### **2. Estrutura dos Arquivos**

```
.
├── main.py                # Código principal para executar o algoritmo genético
├── Individuo.py           # Classe Individuo
├── Populacao.py           # Classe Populacao
├── Produto.py             # Classe Produto
└── mysql_connection.py    # Conexão com o banco de dados MySQL
```

### **3. Banco de Dados**

Certifique-se de ter uma tabela `produtos` no MySQL com a seguinte estrutura:

```sql
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    espaco FLOAT,
    valor FLOAT,
    quantidade INT
);
```

Insira alguns produtos para teste:

```sql
INSERT INTO produtos (nome, espaco, valor, quantidade) VALUES 
('Produto A', 0.5, 100, 3),
('Produto B', 1.0, 300, 2),
('Produto C', 0.3, 150, 5);
```

### **4. Executar o Código**

```bash
python main.py
```

---

## 📊 Gráfico do Melhor Fitness por Geração

O código gera um gráfico mostrando o progresso do melhor fitness em cada geração. O gráfico será salvo como `melhor_fitness_por_geracao.png` e exibido ao final da execução.

Exemplo de gráfico gerado:

![Melhor Fitness por Geração](melhor_fitness_por_geracao.png)

---

## 🔍 Resultados das Execuções

### **Execução 1**

- **Melhor Fitness**: `950`
- **Produtos Transportados**: `['Produto A', 'Produto B', 'Produto C']`
- **Geração do Melhor Fitness**: `342`

### **Execução 2**

- **Melhor Fitness**: `870`
- **Produtos Transportados**: `['Produto B', 'Produto C']`
- **Geração do Melhor Fitness**: `295`

### **Execução 3**

- **Melhor Fitness**: `920`
- **Produtos Transportados**: `['Produto A', 'Produto C']`
- **Geração do Melhor Fitness**: `415`

---

## 🛠️ Detalhes Técnicos

- **Número de Gerações**: `500`
- **Tamanho da População**: `20`
- **Taxa de Mutação**: `1%`
- **Limite de Espaço**: `3.0`

---

## 📝 Autor

- **Fabio Oliveira**
