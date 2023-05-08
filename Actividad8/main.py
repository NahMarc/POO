from conjunto import Conjunto


def test():

    conjuntoA = Conjunto([1, 2, 3, 4])
    conjuntoB = Conjunto([3, 6, 9])
    conjuntoC = Conjunto([1, 2, 3, 4])

    assert conjuntoA == conjuntoC
    assert conjuntoA != conjuntoB
    assert conjuntoA + conjuntoB == Conjunto([1, 2, 3, 4, 6, 9])
    assert conjuntoA - conjuntoB == Conjunto([1, 2, 4])


if __name__ == '__main__':

    test()

    conjuntoA = Conjunto([1, 2, 3, 4])
    conjuntoB = Conjunto([3, 6, 9])
    conjuntoC = Conjunto([1, 2, 3, 4])

    print("Conjunto A:", conjuntoA)
    print("Conjunto B:", conjuntoB)
    print("Conjunto C:", conjuntoC)
    print("A + B:",  conjuntoA +  conjuntoB)
    print("A - B:",  conjuntoA -  conjuntoB)
    print("A == B:", conjuntoA == conjuntoB)
    print("A == C:", conjuntoA == conjuntoC)
