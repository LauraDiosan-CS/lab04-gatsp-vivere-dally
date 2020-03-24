def read_adjacency_matrix(path):
    net = {}
    with open(path, "r") as cin:
        n = int(cin.readline())
        net['no_nodes'] = n
        mat = []
        for i in range(n):
            mat.append([])
            for e in cin.readline().split(','):
                mat[-1].append(int(e))
        net['mat'] = mat
    return net


def read_int(text):
    """
    Function that reads and validates an integer
    Function won't stop until the read input is an integer
    :param text: the text displayed to the user
    :return: the integer read
    """
    while True:
        try:
            integer = int(input(text))
            return integer
        except ValueError:
            print("The value must be an integer!")


def fitness(perm, mat):
    """
    :param perm: permutation
    :param mat: 2d array of floats
    :return: sum of a permutation of indices from an adjacency matrix
    """
    f = 0.0
    prev = perm[0]
    for cur in perm[1:]:
        f += mat[prev][cur]
        prev = cur
    return f
