
class Connect:
    forw = {}
    back = {}

    def __init__(self, key: int):
        self.__key = key

    def addTo(self, key: int , w: float):
        Connect.forw[key] = w

    def addFrom(self, key: int ,w: float):
        Connect.back[key] = w

    def getW(self, dest: int) -> float:
        return  Connect.forw.get(dest)

    def getForw(self) -> dict:
        return Connect.forw

    def getBack(self) -> dict:
        return Connect.back

    def getKey(self) -> int:
        return self.__key

    def removeForw(self, key: int) -> bool:
        if Connect.forw.get(key) != None:
            Connect.forw.pop(key)
            return True
        return False
def removeBack(self, key: int) -> bool:
    if Connect.back.get(key) != None:
        Connect.back.pop(key)
        return True
    return False





