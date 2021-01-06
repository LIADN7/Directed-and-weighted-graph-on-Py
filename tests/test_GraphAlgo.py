from unittest import TestCase
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

def create_graph():
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
    return grp

class TestGraphAlgo(TestCase):
    def test_bfs1(self):
        g = create_graph()
        algo = GraphAlgo(g)
        for i, j in g, algo.get_graph():
            print(i, j)

