import random
import numpy as np

from Produto import Produto


class Individuo:
    def __init__(self, produtos:list[Produto], limite_espaco:float, cromossomos=[]):
        self.produtos = produtos
        self.limite_espaco = limite_espaco
        self.cromossomos = cromossomos
        self.fitness = 1

    def inicializar_individuo(self):
        self.cromossomos = [random.randint(0, 1) for _ in self.produtos]

    def avaliar_individuo(self):
        fitness = 0
        espaco = 0

        for i, escolha in enumerate(self.cromossomos):

            if escolha == 1:

                produto = self.produtos[i]

                fitness += produto.valor
                espaco += produto.espaco

        if espaco > self.limite_espaco:
            fitness = 1
        
        self.fitness = fitness

        return fitness
    
    def listar_produtos(self):
        produtos_levados = []

        for i, produto in enumerate(self.produtos):
            if self.cromossomos[i] == 1:
                produtos_levados.append(produto.nome)

        return produtos_levados

