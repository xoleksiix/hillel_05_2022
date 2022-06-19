from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    """Change me"""

    def draw(self):
        print("----", "|  |", "----", sep="\n")


class Circle(Shape):
    """Change me"""

    def draw(self):
        print(" -- ", "-  -", " -- ", sep="\n")


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle
    """
    options: list[Shape] = [Rectangle, Circle]
    return choice(options)


def main():
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    # I don't know how best to initialize

    # shape: Shape = get_shape()
    # random_shape = shape()
    # random_shape.draw()

    shape: Shape = get_shape()()
    shape.draw()


if __name__ == "__main__":
    main()
