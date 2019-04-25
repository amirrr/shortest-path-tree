import time
from tqdm import tqdm
import random
import numpy as np
# using tqdm on itterable elemets let you see progress bar for it

#for i in tqdm(range(10)):
    #sys.stdout.write("\r{0}>".format("="*i))
    #sys.stdout.flush()

class Node(object):
    """Return the square root of self times self."""

    def __init__(self, data, vtd):
        self.data = data
        self.children = []
        self.visited = set()
        self.visited.update(vtd)

    def add_child(self, obj):
        """ add new node to list of children """
        self.children.append(obj)

def possible_nodes(start_finish, visited):
    """ look for possible node expantion based on visited nodes """
    result = set()
    for start in start_finish:
        if start in visited:
            if not start_finish[start] in visited:      # if destination is not visited
                result.add(start_finish[start])         # add it to the possible nodes
        else:
            result.add(start)       # if start is not visited its a possible node to visit
    return result

def main():
    matris = []
    number_city = 6

    origin_destination = {1: 4, 2: 5, 3: 6}

    for i in range(number_city):
        abas = []
        for j in range(number_city):
            if i == j:
                abas.append(0)
            else:
                abas.append(random.randint(5, 30))
        matris.append(abas)

    print(np.matrix(matris))
    # print()

if __name__ == "__main__":
    main()
