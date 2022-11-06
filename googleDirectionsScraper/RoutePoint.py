class RoutePoint:
    def __init__(self, name, id, lat, long) -> None:
        self.__name = name
        self.__id = id
        self.__loc = [lat, long]

    def __repr__(self) -> str:
        return f'name: {self.__name} id: {self.__id} lat: {self.__loc[0]} long: {self.__loc[1]}\n'

    def __eq__(self, __o: object) -> bool:
        return self.__loc[0] == __o.__loc[0] and self.__loc[1] == __o.__loc[1]

    def getCoordinates(self):
        return f'{self.__loc[0]}, {self.__loc[1]}'