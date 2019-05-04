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
    source_dest = {}
    distance_matix = []
    def __init__(self, data, vtd, distance):
        self.data = data
        self.children = []
        self.visited = set()
        self.visited.update(vtd)
        self.distance = distance

    def create_children(self):
        """ creat the node children and return them if any, false otherwise """
        univisited_set = possible_nodes(Node.source_dest, self.visited)
        if len(univisited_set) != 0:
            for i in univisited_set:
                temp_visited_set = set(self.visited)
                temp_visited_set.add(i)
                temp_distance = self.distance + Node.distance_matix[self.data-1][i-1]
                node = Node(i, temp_visited_set, temp_distance)
                self.children.append(node)
            return self.children
        else:
            return False


    def add_child(self, obj):
        """ add new node to list of children """
        self.children.append(obj)

    def get_child(self):
        """ return this nodes children """
        return self.children

    def print_data(self):
        """ print list of children """
        print('mother:', self.data, '----> ', end='')
        for child in self.children:
            print(child.data, end=' ')
        print('')

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

    Node.source_dest = origin_destination
    Node.distance_matix = matris

    mother_node = Node(0, [], 0)
    c1 = Node(1, [1], 10)
    c2 = Node(2, [2], 10)
    c3 = Node(3, [3], 10)
    mother_node.add_child(c1)
    mother_node.add_child(c2)
    mother_node.add_child(c3)
    mother_node.print_data()

    #print(possible_nodes(origin_destination, c1.visited))

    c1child = c1.create_children()
    c1.print_data()

    for i in c1child:
        i.create_children()
        i.print_data()


if __name__ == "__main__":
    main()
