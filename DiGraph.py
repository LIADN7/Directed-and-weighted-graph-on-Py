from GraphInterface import GraphInterface
from Node import Node

class DiGraph(GraphInterface):

    def __init__(self):
        self.__nodes = {}
        self.__edgeSize = 0
        self.__nodeSize = 0
        self.__change = 0

    def __str__(self):
        return f"{{nodes: [{self.__nodes}], edgeSize: {self.__edgeSize}, nodeSize: {self.__nodeSize}, change: {self.__change}}}"

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """
        return self.__nodeSize

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        return self.__edgeSize

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair  (key, node_data)
        """
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (key, weight)
         """
        temp = self.getNode(id1)
        if temp != None:
            return temp.getBack()
        return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
        weight)
        """
        temp = self.getNode(id1)
        if temp != None:
            return temp.getForw()
        return None

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.__change

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if self.getNode(id1) == None or self.getNode(id2) == None or id1 == id2:
            return False
        t1 = self.getNode(id1)
        t2 = self.getNode(id2)
        t1.addTo(id2, weight)
        t2.addFrom(id1, weight)
        self.__edgeSize += 1
        self.__change += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if self.__nodes.get(node_id) == None:
            self.__nodes[node_id] = Node(node_id)
            self.__nodeSize += 1
            self.__change += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if self.getNode(node_id) != None:
            forw = self.all_out_edges_of_node(node_id).keys()
            back = self.all_in_edges_of_node(node_id).keys()
            for i in forw:
                self.remove_edge(node_id, i)
            for i in back:
                self.remove_edge(i, node_id)
            self.__nodes.pop(node_id)
            self.__nodeSize -= 1
            self.__change += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if self.getNode(node_id1) == None or self.getNode(node_id2) == None or node_id1 == node_id2:
            return False
        temp = self.all_out_edges_of_node(node_id1)
        if temp.get(node_id2)  != None:
            t1 = self.getNode(node_id1)
            t2 = self.getNode(node_id2)
            t1.removeForw(node_id2)
            t2.removeForw(node_id1)
            self.__edgeSize -= 1
            self.__change += 1
            return True
        return False

    def getNode(self, id1: int) -> Node:
        """
        return a Node
        """
        return self.__nodes.get(id1)

