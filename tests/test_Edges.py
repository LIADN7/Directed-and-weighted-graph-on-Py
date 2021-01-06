from unittest import TestCase
from Edges import Edges

class TestEdges(TestCase):
    def test_edge_getData(self):
        e = Edges(1, 2, 5.2)
        self.assertEqual(e.getSrc(), 1)
        self.assertEqual(e.getDest(), 2)
        self.assertEqual(e.getWeight(), 5.2)
        print(e)
