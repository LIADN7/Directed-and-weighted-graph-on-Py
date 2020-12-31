from DiGraph import DiGraph
from Location import Location
from Node import Node



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
x = grp.all_out_edges_of_node(2).keys()
print(grp.all_out_edges_of_node(2))
print(grp.remove_node(2))
print(grp.all_out_edges_of_node(2))

