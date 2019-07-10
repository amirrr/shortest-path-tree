from datetime import datetime
import random
import os
import numpy as np
import psutil
import pandas
import matplotlib.pyplot as plt
from table import checkerboard_table


# from tqdm import tqdm
# using tqdm on itterable elemets let you see progress bar for it

#for i in tqdm(range(10)):
    #sys.stdout.write("\r{0}>".format("="*i))
    #sys.stdout.flush()

class Node(object):
    """Return the square root of self times self."""
    source_dest = {}
    distance_matix = []
    max_distance = 0

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
                # if Node.distance_matix[self.data-1][i-1] == Node.max_distance:
                #     continue
                temp_distance = self.distance + Node.distance_matix[self.data-1][i-1]
                temp_visited_set = list(self.visited)
                temp_visited_set.append(i)
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
        print('order of travers:', self.visited, '----> distance:', self.distance)
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

def generate_mother_node(number_of_users):

    ori_dest = {}
    mother_node = Node(0, [], 0)

    for user in range(1, number_of_users+1):
        ori_dest[user] = number_of_users + user
        mother_node.add_child(Node(user, [user], 10))

    return ori_dest, mother_node


def main():
    process = psutil.Process(os.getpid())
    matris = []
    number_users = 3
    number_city = number_users*2

    for i in range(number_city):
        abas = []
        for j in range(number_city):
            if i == j:
                abas.append(0)
            else:
                abas.append(random.randint(5, 30))
        matris.append(abas)

    print('distance matris created!')
    max_dis = 0
    for i in matris:
        for j in i:
            if j > max_dis:
                max_dis = j
    
    mother = Node(0, [], 0)
    origin_destination, mother = generate_mother_node(number_users)
    Node.source_dest = origin_destination
    Node.distance_matix = matris
    Node.max_distance = max_dis


    results = list()
    queue = list()
    queue.extend(mother.get_child())
    number_of_nodes = 0

    start_time = datetime.now()
    while(len(queue)!=0):
        number_of_nodes = number_of_nodes+1
        temp_node = queue.pop(0)
        if temp_node.create_children():
            queue.extend(temp_node.get_child())
        else:
            results.append(temp_node)

    print('nodes created finding shortest path')
    
    # sort the list by distance
    #results.sort(key=lambda x: x.distance, reverse=False)
    first = min(results, key=lambda x: x.distance)

    print('total nodes:', number_of_nodes, ' - total ways to travers:', len(results))

    #first, last = results[:1], results[-1]

    print('shortest distance ', end='')
    first.print_data()

    temp_matris = list(map(list, matris))

    for i in range(number_city-1):
        x = first.visited[i] - 1
        y = first.visited[i+1] - 1
        temp_matris[x][y] = 0

    data1 = pandas.DataFrame(np.matrix(temp_matris))
    checkerboard_table(data1, matris)

    #print(np.matrix(matris))
    #print(np.matrix(temp_matris))

    print('max in matrix:', max_dis)
    print('total size:', process.memory_info().rss/1024)
    print('total time:', datetime.now() - start_time)
    plt.show()




if __name__ == "__main__":

    main()
