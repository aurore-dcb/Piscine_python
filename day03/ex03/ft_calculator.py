class calculator:

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object) -> None:
        self.vector = [elem + object for elem in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [elem * object for elem in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [elem - object for elem in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        try:
            assert object != 0, "division by zero"
            self.vector = [elem / object for elem in self.vector]
            print(self.vector)
        except AssertionError as msg:
            print("AssertionError:", msg)
            exit(1)
