import random

from Individuo import Individuo
from Produto import Produto


class Populacao:
    def __init__(self, populacao:int, individuos:list[Individuo], produtos:list[Produto], taxa_de_mutacao:float):
        self.produtos = produtos
        self.populacao = populacao
        self.individuos = individuos
        self.taxa_de_mutacao = taxa_de_mutacao
        self.geracao = 0

    def avaliar_populacao(self):
        for individuo in self.individuos:
            individuo.avaliar_individuo()

        self.melhor_individuo = max(self.individuos, key=lambda individuo: individuo.fitness)
        self.melhor_fitness = self.melhor_individuo.fitness
        

    def somar_fitness_total(self):
        #print([individuo.fitness for individuo in self.individuos])
        return sum(individuo.fitness for individuo in self.individuos)

    def selecionar_pais(self):
        soma_fitness = self.somar_fitness_total()
        probabilidades = [individuo.fitness / soma_fitness for individuo in self.individuos]
        pais_selecionados = random.choices(self.individuos, weights=probabilidades, k=2)

        return pais_selecionados

    def crossover_mutacao(self):
        nova_populacao = []

        for i in range(self.populacao//2):
            ponto_de_corte = random.randint(1, len(self.individuos[0].cromossomos)-1)

            pais = self.selecionar_pais()

            cromossomo_filho1 = pais[0].cromossomos[:ponto_de_corte] + pais[1].cromossomos[ponto_de_corte:]
            cromossomo_filho2 = pais[1].cromossomos[:ponto_de_corte] + pais[0].cromossomos[ponto_de_corte:]

            filho1 = Individuo(produtos=self.produtos, 
                               cromossomos=cromossomo_filho1, 
                               limite_espaco=self.individuos[0].limite_espaco)
            
            filho2 = Individuo(produtos=self.produtos, 
                               cromossomos=cromossomo_filho2, 
                               limite_espaco=self.individuos[0].limite_espaco)

            nova_populacao.append(filho1)
            nova_populacao.append(filho2)

        for individuo in nova_populacao:
            for i in range(len(individuo.cromossomos)):
                if random.random() < self.taxa_de_mutacao:
                    individuo.cromossomos[i] = 1 if individuo.cromossomos[i] == 0 else 0

        self.geracao += 1

        self.individuos = nova_populacao