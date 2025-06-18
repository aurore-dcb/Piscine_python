class calculator:
    """ calculator class """

    def __init__(self, vector):
        """ Constructor (calculator) """
        self.vector = vector

    def __add__(self, object) -> None:
        """ Add an object to each element of the vector """
        self.vector = [elem + object for elem in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """ Multiply each element of the vector by an object """
        self.vector = [elem * object for elem in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """ Subtract an object from each element of the vector """
        self.vector = [elem - object for elem in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """ Divide each element of the vector by an object """
        try:
            assert object != 0, "division by zero"
            self.vector = [elem / object for elem in self.vector]
            print(self.vector)
        except AssertionError as msg:
            print("ZeroDivisionError:", msg)
            return
