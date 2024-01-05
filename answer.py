"""importing solver function from solver file"""
from solver import solver


def answer():
    """calling solver function from solver file"""
    return solver(100)


if __name__ == "__main__":
    print(answer())
