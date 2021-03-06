'''
Implementation of Graph Overview
In this lecture we will implement a simple graph by focusing on the Node class. Refer to this lecture for the solution to the Interview Problem

The graph will be directed and the edges can hold weights.

We will have three classes, a State class, a Node class, and finally the Graph class.

We're going to be taking advantage of two built-in tools here, OrderDict and Enum
'''

from enum import Enum  

class State(Enum):
    unvisited = 1 #White
    visited = 2 #Black
    visiting = 3 #Gray

#Now for the Node class we will take advantage of the OrderedDict object in case we want to keep trak of the order keys are added to the dictionary.

from collections import OrderedDict

class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node, val = weight

    def __str__(self):
        return str(self.num)

class Graph:

    def __init__(self):
        self.nodes = OrderedDict()  # key = node id, val = node

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):
        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)
        self.nodes[source].adjacent[self.nodes[dest]] = weight

g = Graph()
g.add_edge(0, 1, 5)

print (g.nodes)
#OrderedDict([(0, <__main__.Node instance at 0x103a761b8>),(1, <__main__.Node instance at 0x104dfef80>)])