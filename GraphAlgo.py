from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from Node import Node
import json

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, grp: DiGraph):
        self.__grp = grp

    def get_graph(self) -> DiGraph:
        return self.__grp

    def load_from_json(self, file_name: str) -> bool:
        dict_graph = {}
        try:
            with open(file_name, "r") as file:
                dict_graph = json.load(fp=file)
                for k, v in dict_graph.item():
                    g = DiGraph(**v)
                    # add to init of DiGraph - **kwargs
                    dict_graph[k] = g
        except IOError as e:
            print(e)
        self.__grp = dict_graph

    def save_to_json(self, file_name: str) -> bool:
       try:
           with open (file_name, "w") as file:
               json.dump(self.__grp, default=lambda m: m.as_dict, fp=file, indent=4)
       except IOError as e:
           print(e)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.__grp.getNode(id1) == None or self.__grp.getNode(id2) == None:
            return None
        q = []
        if id1 == id2:
            return (0, [id1])
        temp_dict = self.bfs(id1, id2)
        if self.__grp.getNode(id2).getPrev() != -1:
            s = self.__grp.getNode(id2).getWeight()
            t = self.__grp.getNode(id2)
            q.append(id2)
            while t.getPrev() != -1:
                pre = t.getPrev()
                t.setPrev(-1)
                t.setWeight(0)
                q.insert(0, pre)
                t = self.__grp.getNode(pre)
            t.setWeight(0)
            lis = (s-1, q)
            return lis
        for i in temp_dict:
            t = self.__grp.getNode(i)
            t.setWeight(0)
            t.setPrev(-1)
        return q

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        raise NotImplementedError

    def connected_components(self): # -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        raise NotImplementedError

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError

    def bfs(self, src: int, des: int):
        map_dict = []
        qem = []
        self.__grp.getNode(src).setWeight(1)
        map_dict.append(src)
        qem.append(src)
        way = -1
        for i in qem:
            b = False
            poll = i
            weight = self.__grp.getNode(i).getWeight()
            for j in self.__grp.all_out_edges_of_node(i):
                count = self.__grp.getNode(i).getW(j) + weight
                n = self.__grp.getNode(j)
                if j == des and (way > count or way == -1):
                    way = count
                    n.setWeight(way)
                    n.setPrev(i)
                    map_dict.append(n.getKey())
                    b = True
                elif (n.getWeight() > count or n.getWeight() == 0) and b == False:
                    n.setWeight(count)
                    n.setPrev(i)
                    qem.append(n.getKey())
                    map_dict.append(n.getKey())
        return map_dict
