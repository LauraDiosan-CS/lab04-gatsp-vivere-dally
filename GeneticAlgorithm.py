from random import random, uniform, randint, seed

from lab04.PermChromosome import Chromosome


class GA:
    def __init__(self, param=None):
        self.__pop = []
        self.__param = param
        seed()

    def initialization(self):
        for _ in range(self.__param['pop_size']):
            c = Chromosome(self.__param)
            c.initialize()
            self.__pop.append(c)

    def evaluation(self):
        for c in self.__pop:
            c.fitness = self.__param['fit_func'](c.representation, self.__param['mat'])

    def __get_prob(self, s, i):
        p = self.__param['pop_size']
        return ((2 - s) / p) + ((2 * i * (s - 1)) / (p * (p - 1)))

    def selection(self):
        s = 1 + random()
        probs = [self.__get_prob(s, self.__pop[0].fitness)]
        for c in self.__pop[1:]:
            probs.append(probs[-1] + self.__get_prob(s, c.fitness))
        prob = uniform(0, probs[-1])
        chosen = -1
        for i in range(self.__param['pop_size'] - 1):
            if probs[i] <= prob < probs[i + 1]:
                chosen = i
                break
        return chosen

    # def selection(self):
    #     pos1 = randint(0, self.__param['pop_size'] - 1)
    #     pos2 = randint(0, self.__param['pop_size'] - 1)
    #     if self.__pop[pos1].fitness < self.__pop[pos2].fitness:
    #         return pos1
    #     return pos2

    def best_chromosome(self):
        best = self.__pop[0]
        for c in self.__pop:
            if c.fitness < best.fitness:
                best = c
        return best

    def worst_chromosome(self):
        worst = self.__pop[0]
        for c in self.__pop:
            if c.fitness > worst.fitness:
                worst = c
        return worst

    def one_generation(self):
        new_population = [self.best_chromosome()]
        for _ in range(self.__param['pop_size'] - 1):
            c1 = self.__pop[self.selection()]
            c2 = self.__pop[self.selection()]
            off = c1.crossover(c2)
            off.mutation()
            new_population.append(off)
        self.__pop = new_population
        self.evaluation()
