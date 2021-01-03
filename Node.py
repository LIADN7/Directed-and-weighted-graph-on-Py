from Location import Location


class Node:
    defKey = 0

    def __init__(self, Key: int,  local=Location(0.0, 0.0, 0.0), tag=0, nw=0.0, info="", **kwargs):
        self.__key = Key
        self.__local = local
        self.__tag = tag
        self.__nw = nw
        self.__info = info
        self.__forw = dict()
        self.__back = dict()
        self.__prev = -1

    def __str__(self) -> str:
        return f"\"id\": {self.__key}, \"pos\": {self.__local}"

    def __repr__(self) -> str:
        return f"{{\"id\": {self.__key}, \"pos\": {self.__local}}}"

    def getKey(self) -> int:
        return self.__key

    def getLocal(self) -> Location:
        return self.__local

    def setLocal(self, local: Location):
        self.__local = local

    def getWeight(self) -> float:
        return self.__nw

    def setWeight(self, nw: float):
        self.__nw = nw

    def getInfo(self) -> str:
        return self.__info

    def setInfo(self, info: str):
        self.__info = info

    def getTag(self) -> int:
        return self.__tag

    def setTag(self, tag: str):
        self.__tag = tag

    def addTo(self, key: int, w: float):
        self.__forw[key] = w

    def addFrom(self, key: int, w: float):
        self.__back[key] = w

    def getW(self, dest: int) -> float:
        return self.__forw.get(dest)

    def getForw(self) -> dict:
        return self.__forw.copy()

    def getBack(self) -> dict:
        return self.__back.copy()

    def getKey(self) -> int:
        return self.__key

    def removeForw(self, key: int) -> bool:
        if self.__forw.get(key) != None:
            self.__forw.pop(key)
            return True
        return False

    def removeBack(self, key: int) -> bool:
        if self.__back.get(key) != None:
            self.__back.pop(key)
            return True
        return False

    def getPrev(self):
        return self.__prev

    def setPrev(self, prev: int):
        self.__prev = prev


