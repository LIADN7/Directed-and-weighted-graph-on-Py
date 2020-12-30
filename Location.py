import Location as Location


class Location:
    def __init__(self,  x=0.0, y=0.0, z=0.0):
        self.__x = x
        self.__y = y
        self.__z = z

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def z(self):
        return self.__z

    def dist(self, g: Location):
        dis = (self.__x - g.__x)**2 + (self.__y - g.__y)**2 +(self.__z - g.__z)**2
        dis = dis**(0.5)
        return dis
