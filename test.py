import time
from tqdm import tqdm
import random
import numpy as np
from sys import getsizeof
from datetime import datetime


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
        #self.visited = set()
        self.visited = []
        self.visited.extend(vtd)
        self.distance = distance

    def create_children(self):
        """ creat the node children and return them if any, false otherwise """
        univisited_set = possible_nodes(Node.source_dest, self.visited)
        if len(univisited_set) != 0:
            for i in univisited_set:
                temp_visited_set = list(self.visited)
                temp_visited_set.append(i)
                temp_distance = self.distance + Node.distance_matix[self.data-1][i-1]
                node = Node(i, temp_visited_set, temp_distance)
                self.children.append(node)
            return True
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
        print('order of travers:', self.visited, '----> ', self.distance)
        #for child in self.children:
        #    print(child.data, child.visited, child.distance, end='\t')
        #print('')

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
    number_city = 10

    origin_destination = {1: 6, 2: 7, 3: 8, 4: 9, 5: 10 }

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
    c4 = Node(4, [4], 10)
    c5 = Node(5, [5], 10)
    mother_node.add_child(c1)
    mother_node.add_child(c2)
    mother_node.add_child(c3)
    mother_node.add_child(c4)
    mother_node.add_child(c5)
    for c in mother_node.get_child():
        c.print_data()
    

    results = list()
    queue = list()
    queue.append(c1)
    queue.append(c2)
    queue.append(c3)
    queue.append(c4)
    queue.append(c5)
    a = 0

    startTime = datetime.now()
    while(len(queue)!=0):
        a = a+1
        temp_node = queue.pop(0)
        if temp_node.create_children():
            queue.extend(temp_node.get_child())
        else:
            results.append(temp_node)
    
    # sort the list by distance
    results.sort(key=lambda x: x.distance, reverse=True)
    print('total nodes:', a)

    first, last = results[0], results[-1]
    first.print_data()
    last.print_data()
    print('total time:', datetime.now() - startTime)




if __name__ == "__main__":
    main()