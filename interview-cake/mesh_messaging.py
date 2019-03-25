import networkx as nx
import matplotlib.pyplot as plt
import random

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()

    def __str__(self):
        return self.label

graph_raw = [
    ('Min', ['William', 'Jayden', 'Omar']),
    ('William', ['Min', 'Noam']),
    ('Jayden', ['Min', 'Amelia', 'Ren', 'Noam']),
    ('Ren', ['Jayden', 'Omar']),
    ('Amelia', ['Jayden', 'Adam', 'Miguel']),
    ('Adam', ['Amelia', 'Miguel']),
    ('Miguel', ['Amelia', 'Adam']),
    ('Noam', ['Jayden', 'William']),
    ('Omar', ['Ren', 'Min'])]


color_list = ['blue', 'green', 'yellow', 'red', 'brown', 'violet', 'pink']

nodes = {}

for node_label, _ in graph_raw:
    nodes[node_label] = GraphNode(node_label)

for node_label, neighbor_labels in graph_raw:
    node = nodes[node_label]

    for i in neighbor_labels:
        node.neighbors.add(nodes[i])

# basic idea:
# we start from Jayden and need to find a route to adam
# we start with Jayden

# then we do dfs?
# bfs - as it guarantess us to find shortest path
# bfs guqrantess shortest path at it moves layer on layer like onion 
# not favouriting any path

# this if of course for unwighted (in weighted scenario we would need ot use jikstra)
# and not directed graph

# to do bfs we need to use queue -> pop(0) and append in python
# (stack is used for dfs)

# iterative version can be usefull to find is there exist a value
# but how to create a route? with recurrence this potentialy would be easy - just 'backtrack'

nodes_queue = [nodes['Jayden']]

while len(nodes_queue):
    current_node = nodes_queue.pop(0)

    if current_node.label == 'Adam':
        print 'found Adam'
        break

    for n in current_node.neighbors:
        nodes_queue.append(n)

# code to genearte graph and plot it
G = nx.Graph()

for node_key in nodes:
    node = nodes[node_key]
    G.add_node(node)
    for i in node.neighbors:
        G.add_edge(node, i)

nx.draw(G, with_labels = True, node_color='white')
plt.show()
