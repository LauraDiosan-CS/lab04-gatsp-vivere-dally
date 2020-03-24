from lab04.GeneticAlgorithm import GA


class Simulator:
    def __init__(self, param=None, path=None):
        self.__param = param
        self.__path = path
        self.__ga = GA(param)
        self.__ga.initialization()
        self.__ga.evaluation()

    def __plot(self):
        # TODO
        None

    def simulate(self):
        s = ''
        for gen in range(self.__param['no_gens']):
            print("Gen " + str(gen) + " of " + str(self.__param['no_gens']))
            local_best = self.__ga.best_chromosome()
            s += str(local_best)
            self.__ga.one_generation()

        with open(self.__path, 'w') as cout:
            cout.write(s)
            cout.flush()
