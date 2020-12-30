from Location import Location


class Node:
    defKey=0


    def __init__(self,  local: Location, tag=0, nw=0.0, info=""):
        self.__key = Node.defKey
        Node.defKey = Node.defKey + 1
        self.__local = local
        self.__tag = tag
        self.__nw = nw
        self.__info = info

    def getKey(self) -> int:
        return self.__key

    def getLocal(self):
        return self.__local

    def setLocal(self, local: Location):
        self.__local=local

    def getWeight(self) -> float:
        return self.__nw

    def setWeight(self, nw: float):
        self.__nw=nw

    def getInfo(self) -> str:
        return self.__info

    def setInfo(self, info: str):
        self.__info = info

    def getTag(self) -> int:
        return self.__tag

    def setTag(self, tag: str):
        self.__tag = tag






