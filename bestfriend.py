class Person:
    def __init__(self, name):
        self.__name = name
        self.__bestfriend = None

    @property
    def name(self):
        return self.__name

    @property
    def bestfriend(self):
        return self.__bestfriend

    @bestfriend.setter
    def bestfriend(self, bestfriend):
        self.__bestfriesnd = bestfriend
        bestfriend.__bestfriend = self
anichka = Person("Anichka")
andrae = Person("Andrae")
anichka.bestfriend = andrae
print(anichka.bestfriend.name)
print(andrae.bestfriend.name)
