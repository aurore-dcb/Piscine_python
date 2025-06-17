class calculator:
    """ calculator class """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ Calculate the dot product of two vectors """
        res = sum(elemV1 * elemV2 for elemV1, elemV2 in zip(V1, V2))
        print("Dot product is: " + str(res))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """ Add two vectors element-wise """
        res = [float(elemV1 + elemV2) for elemV1, elemV2 in zip(V1, V2)]
        print("Add vector is:", res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """ Subtract two vectors element-wise """
        res = [float(elemV1 - elemV2) for elemV1, elemV2 in zip(V1, V2)]
        print("Add vector is:", res)
