import logging

logging.basicConfig(filename="friend.log", level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')

class Friendship:
    """A simple class"""

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

        logging.info("Friend Name-Age: {} - {}".format(self.fullname, self._age))

    @property
    def age(self):
        return "{}.".format(self._age)

    @property
    def fullname(self):
        return "{} {}.".format(self.first, self.last)


friend1 = Friendship("Yunus", "Emre", 30)
friend2 = Friendship("Efe", "Goalkeeper", 10)
friend3 = Friendship("Mr", "Özdemir", 20)
