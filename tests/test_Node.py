from unittest import TestCase
from Node import Node

node = Node(1)

class TestNode(TestCase):

    def test_getKey(self):
        self.assertEqual(node.getKey(), 1)

    """
    wait for new commit
    
    def test_getLocal(self):
        node = Node(1)
        node.setLocal()
        self.assertEqual(node.getKey(), 1)

    """

    def test_getWeight(self):
        node.setWeight(5.1)
        self.assertEqual(node.getWeight(), 5.1)

    def test_getInfo(self):
        node.setInfo("good")
        self.assertEqual(node.getInfo(), "good")

    def test_getTag(self):
        node.setTag(4)
        self.assertEqual(node.getTag(), 4)

    def test_getPrev(self):
        node.setPrev(7)
        self.assertEqual(node.getPrev(), 7)

    def test_addTo_getW_getForw(self):
        node.addTo(2, 0.23)
        node.addTo(7, 1.3)

        self.assertEqual(node.getW(2), 0.23)
        self.assertEqual(node.getW(7), 1.3)
        for i in node.getForw():
            if i != 2 and i != 7:
                self.assertEqual(i, 2)

    def test_addFrom_getBack(self):
        node = Node(1)
        node.addFrom(5, 2)
        node.addFrom(4, 9)
        node.addTo(13, 2.2)
        for i in node.getBack():
            if i != 5 and i != 4:
                self.fail("not good")

    def test_removeForw_removeBack(self):
        node.addTo(2, 0.23)
        node.addTo(7, 1.3)
        node.addTo(8, 1.3)
        node.removeForw(8)
        node.addFrom(5, 2)
        node.addFrom(4, 9)
        node.removeBack(12)
        for i in node.getForw():
            self.assertNotEqual(i, 8)
        for i in node.getBack():
            self.assertNotEqual(i, 12)



