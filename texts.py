from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
from Edges import Edges
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

print(algo.get_graph().getNode(2).getW(3))
"""


grp = DiGraph()
grp.add_node(0)
grp.add_node(1)
grp.add_node(2)
grp.add_node(3)
grp.add_node(4)
grp.add_node(5)
grp.add_node(6)
grp.add_node(7)
grp.add_node(8)
grp.add_node(9)

"print(grp.get_all_v())"

grp.add_edge(9, 8, 1)
grp.add_edge(8, 9, 1)
grp.add_edge(1, 2, 1)
grp.add_edge(2, 6, 2)
grp.add_edge(6, 1, 1)
grp.add_edge(3, 2, 1)
grp.add_edge(3, 7, 1)
grp.add_edge(3, 5, 1)
grp.add_edge(7, 3, 1)
grp.add_edge(5, 4, 1)
grp.add_edge(4, 5, 1)
grp.add_edge(4, 6, 1)
grp.add_edge(8, 4, 1)
grp.add_edge(7, 8, 1)
algo = GraphAlgo(grp)
