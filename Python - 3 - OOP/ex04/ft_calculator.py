
class calculator:
    """
    Represents a calculator that can
    add, multiply and subtract arrays of numbers.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and prints the dot product of two vectors.
        """
        arr = [int(V1[i] * V2[i]) for i in range(len(V1))]
        print(f"Dot Product is: {sum(arr)}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the addition of two vectors and prints the result.
        """
        arr = [float(V1[i] + V2[i]) for i in range(len(V1))]
        print(f"Add Vector is: {arr}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate the substraction of two vectors and prints the result.
        """
        arr = [float(V1[i] - V2[i]) for i in range(len(V1))]
        print(f"Sous Vector is: {arr}")
