import networkx as nx
import matplotlib.pyplot as plt
import random

class GraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = "white"

    def __str__(self):
        return self.label

graph_raw = [
    ('a', ['b', 'd', 'c']),
    ('b', ['a', 'g', 'h']),
    ('c', ['a', 'd', 'e']),
    ('d', ['a', 'c', 'f']),
    ('e', ['j', 'c']),
    ('f', ['d', 'g', 'i']),
    ('g', ['b', 'f', 'h']),
    ('h', ['b', 'g', 'l']),
    ('i', ['j', 'k', 'l', 'f']),
    ('j', ['e', 'i', 'k']),
    ('k', ['i', 'j', 'l']),
    ('l', ['i', 'k', 'h'])
    ]


color_list = ['blue', 'green', 'yellow', 'red', 'brown', 'violet', 'pink']

# maximum degree
max_degree = 0
for _, neighbours in graph_raw:
    if len(neighbours) > max_degree:
        max_degree = len(neighbours)

colors_needed = color_list[:max_degree]
nodes = {}

for node_label, _ in graph_raw:
    nodes[node_label] = GraphNode(node_label)

for node_label, neighbor_labels in graph_raw:
    node = nodes[node_label]

    for i in neighbor_labels:
        node.neighbors.add(nodes[i])

# basic idea:
# for each node traverse neighbours maintaing a list of potential colors
# if neighbour has this color dont take it? and thus remove the list of colors

for node_key in nodes:
    node = nodes[node_key]
    remaining_colors = []
    available = False

    for c in colors_needed:
        available = True
        for n in node.neighbors:
            if n.color == c:
                available = False

        if available:
            remaining_colors.append(c)

    node.color = random.choice(remaining_colors)

# code to genearte graph and plot it
G = nx.Graph()

for node_key in nodes:
    node = nodes[node_key]
    G.add_node(node)
    for i in node.neighbors:
        G.add_edge(node, i)

color_map = []
for node in G:
    color_map.append(node.color)

nx.draw(G, with_labels = True, node_color=color_map)
plt.show()
