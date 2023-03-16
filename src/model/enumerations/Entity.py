from enum import Enum

# class syntax
class Entity(Enum):
    ALEXA = 1
    GOOGLE = 2

    def __eq__(self, other):
        return self.value == other.value