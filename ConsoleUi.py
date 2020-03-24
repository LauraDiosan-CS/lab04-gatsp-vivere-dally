from lab04.Simulator import Simulator
from lab04.utils import read_int, read_adjacency_matrix, fitness


class UI:
    def __init__(self):
        self.__data = {
            0: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\data\\easy_01_tsp.txt",
            1: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\data\\easy_02_tsp.txt",
            2: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\data\\medium_02_tsp.txt",
            3: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\data\\hard_02_tsp.txt",
            4: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\data\\my_test_tsp.txt",
        }
        self.__results = {
            0: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\results\\easy_01_tsp.txt",
            1: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\results\\easy_02_tsp.txt",
            2: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\results\\medium_02_tsp.txt",
            3: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\results\\hard_02_tsp.txt",
            4: "H:\\A_CSUBB\\An2_Sem2\\AI\\Labs\\nCondaPythonLabs\\lab04\\results\\my_test_tsp.txt",
        }

    def __handle_choice(self, choice):
        param = read_adjacency_matrix(self.__data[choice])
        param['node'] = read_int("Enter the start node: ")
        param['pop_size'] = read_int("Enter pop size: ")
        param['no_gens'] = read_int("Enter number of generations: ")
        param['fit_func'] = fitness
        s = Simulator(param, self.__results[choice])
        s.simulate()

    def show_ui(self):
        while True:
            print('1. Easy 1\n' +
                  '2. Easy 2\n' +
                  '3. Medium 2\n' +
                  '4. Hard 2\n' +
                  '5. My test\n'
                  )
            choice = read_int("Enter the test number: ")
            if 1 <= choice <= 5:
                self.__handle_choice(choice - 1)
            else:
                break


if __name__ == '__main__':
    ui = UI()
    ui.show_ui()
