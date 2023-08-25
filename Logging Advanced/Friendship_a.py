import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler("friend_a.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Friendship:
    """A simple class"""

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age

        logger.info("Friend Name-Age: {} - {}".format(self.fullname, self._age))

    @property
    def age(self):
        return "{}.".format(self._age)

    @property
    def fullname(self):
        return "{} {}.".format(self.first, self.last)


friend1 = Friendship("Yunus", "Emre", 30)
friend2 = Friendship("Efe", "Goalkeeper", 10)
friend3 = Friendship("Mr", "Özdemir", 20)
