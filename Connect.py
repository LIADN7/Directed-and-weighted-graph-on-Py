class Connect:

    def _init_(self, key: int):
        self.__key = key
        self.__forw = {}
        self.__back = {}

    def addTo(self, key: int, w: float):
        self.__forw[key] = w

    def addFrom(self, key: int, w: float):
        self.__back[key] = w

    def getW(self, dest: int) -> float:
        return self.__forw.get(dest)

    def getForw(self) -> dict:
        return self.__forw

    def getBack(self) -> dict:
        return self.__back

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