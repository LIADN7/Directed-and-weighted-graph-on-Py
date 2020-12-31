from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
from Location import Location
from Node import Node
import json
"""
grp = DiGraph()
grp.add_node(1)
grp.add_node(2)
grp.add_node(3)
grp.add_node(4)
grp.add_node(5)
grp.add_node(6)
grp.add_node(7)

grp.add_edge(1, 2, 1)
grp.add_edge(2, 3, 0.2)
grp.add_edge(3, 4, 1)
grp.add_edge(4, 5, 1)
grp.add_edge(5, 6, 1)
grp.add_edge(6, 7, 1)
grp.add_edge(7, 1, 1)
grp.add_edge(2, 7, 4)
#algo = GraphAlgo(grp)
print(algo.shortest_path(1, 3))
print(algo.get_graph().getNode(2).getW(3))
"""


grp = DiGraph()
grp.add_node(1)
grp.add_node(2)
grp.add_node(3)
grp.add_node(4)

"print(grp.get_all_v())"

grp.add_edge(2, 1, 1.2)
grp.add_edge(2, 3, 11.2)
grp.add_edge(1, 3, 1.1)
grp.add_edge(3, 4, 1.1)
print(grp.getNode(1))

with open("node_file.txt", "w") as file:
    json.dump(grp.getNode(1).__str__(), fp=file)

with open("graph_file.txt", "w") as file:
    json.dump(grp.__str__(), fp=file)