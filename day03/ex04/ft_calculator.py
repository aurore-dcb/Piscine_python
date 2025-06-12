class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        res = V1[0] * V2[0] + V1[1] * V2[1] + V1[2] * V2[2]
        print("Dot product is: " + str(res))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(elemV1 + elemV2) for elemV1, elemV2 in zip(V1, V2)]
        print("Add vector is:", res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        res = [float(elemV1 - elemV2) for elemV1, elemV2 in zip(V1, V2)]
        print("Add vector is:", res)
