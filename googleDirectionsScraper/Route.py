from json import JSONEncoder

## return object
## startname, startlon, startlat
## endname, endlon, endlat
## distance, polyline



class Route():
    def __init__(self, p1, p2, distance=None, polyline=None) -> None:
        self.__p1 = p1
        self.__p2 = p2
        self.__distance = distance
        self.__polyline = polyline

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2
    
    def __str__(self) -> str:
        return f'p1: {self.__p1} p2: {self.__p2} distance: {self.__distance} polyline: {self.__polyline}'

    def __eq__(self, __o: object) -> bool:
        return self.__p1 == __o.getP1() and self.__p2 == __o.getP2()
