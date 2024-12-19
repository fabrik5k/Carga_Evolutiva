import matplotlib.pyplot as plt

from mysql_connection import consultar_produtos
from Individuo import Individuo 
from Produto import Produto
from Populacao import Populacao

NUM_GERACOES = 500
TAM_POPULACAO = 20
TAXA_MUTACAO = 0.01
ESPACO_LIM = 3.0


if __name__ == '__main__':
    produtos = consultar_produtos()

    arr_produtos = [
        Produto(
            nome=produto[1], 
            espaco=produto[2], 
            valor=produto[3], 
            quantidade=1  # Cada objeto representa uma única unidade
        )
        for produto in produtos
        for _ in range(produto[4])  # Repete de acordo com a quantidade
    ]
    
    arr_individuos = []
    for i in range(TAM_POPULACAO):
        individuo = Individuo(limite_espaco=ESPACO_LIM, produtos=arr_produtos)
        individuo.inicializar_individuo()
        arr_individuos.append(individuo)

    populacao = Populacao(individuos=arr_individuos,
                  populacao=TAM_POPULACAO, 
                  produtos=arr_produtos,
                  taxa_de_mutacao=TAXA_MUTACAO)


    melhor_fitness_por_geracao = []
    melhor_individuo_por_geracao = []

    for geracao in range(NUM_GERACOES):
        populacao.avaliar_populacao()
        populacao.selecionar_pais()
        populacao.crossover_mutacao()

        melhor_fitness_por_geracao.append(populacao.melhor_fitness)
        melhor_individuo_por_geracao.append(populacao.melhor_individuo)




    # Gerar o gráfico do melhor fitness por geração
    plt.figure(figsize=(10, 6))
    plt.plot(range(NUM_GERACOES), melhor_fitness_por_geracao, linestyle='-', color='b')
    plt.title("Melhor Fitness por Geração")
    plt.xlabel("Geração")
    plt.ylabel("Melhor Fitness")
    plt.grid(True)

    # Salvar o gráfico em um arquivo de imagem (ex: PNG)
    plt.savefig("melhor_fitness_por_geracao.png", dpi=300, bbox_inches='tight')
    plt.show()    

    melhor_fitness_geral = max(melhor_fitness_por_geracao)
    indice_melhor_fitness = melhor_fitness_por_geracao.index(melhor_fitness_geral)

    # Encontrar o melhor indivíduo correspondente
    melhor_individuo_geral = melhor_individuo_por_geracao[indice_melhor_fitness]

    # Exibir os resultados
    print(f"Melhor Fitness: {melhor_fitness_geral}")
    print(f"Produtos Levados: {melhor_individuo_geral.listar_produtos()}")
    print(f"Geração do Melhor Fitness: {indice_melhor_fitness}")
    
    
    