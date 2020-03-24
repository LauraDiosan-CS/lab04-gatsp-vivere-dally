from random import shuffle, randint


class Chromosome:
    def __init__(self, param=None):
        self.__rep = []
        self.__fit = 0.0
        self.__param = param

    def initialize(self):
        node = self.__param['node']
        for x in range(self.__param['no_nodes']):
            if x is not node:
                self.__rep.append(x)
        shuffle(self.__rep)
        self.__rep.insert(0, node)
        self.__rep.append(node)

    @property
    def fitness(self):
        return self.__fit

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fit = fit

    @property
    def representation(self):
        return self.__rep

    @representation.setter
    def representation(self, rep=None):
        if rep is None:
            rep = []
        self.__rep = rep

    def crossover(self, other):
        node = self.__param['node']
        rep = [node]
        for i in range(1, self.__param['no_nodes']):
            rep.append(other.__rep[self.__rep[i]])
        rep.append(node)
        off = Chromosome(self.__param)
        off.representation = rep
        return off

    def mutation(self):
        x = randint(0, self.__param['no_nodes'] - 1)
        if x == self.__param['node']:
            return
        self.__rep[self.__rep[x]], self.__rep[x] = self.__rep[x], self.__rep[self.__rep[x]]

    def __str__(self):
        return '\nChromosome: ' + str(self.__rep) + ' has fitness: ' + str(self.__fit)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__rep == other.__rep and self.__fit == other.__fit
