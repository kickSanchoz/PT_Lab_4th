import numpy as np

countN = 85


def initMatrix_v2():
    matrixM_diag = np.arange(3, 171 + 1, 2)
    matrixM = np.diag(np.array(matrixM_diag))
    matrixM[(matrixM == 0)] = 2

    matrixN = np.zeros([countN, countN])
    matrixN[(matrixN == 0)] = 4
    matrixN[::2, 2::3] = 5
    matrixN[1::2, 1::2] = 7

    return matrixM, matrixN


def findF(q, qT, p):
    multQ = np.dot(q, qT)

    f = np.linalg.det(multQ)

    result = np.dot(f, p)
    return result


def findG(matrixM, matrixN, q, qT, p):
    multQ = np.dot(qT, q)

    diagM = np.diag(matrixM)
    diagN = np.diag(matrixN)

    sub = diagM - diagN

    _sum = np.add(sub, multQ)

    result = np.linalg.norm(_sum, 2)

    return result


def initialConditions():
    M, N = initMatrix_v2()

    p = np.full(countN, 1) + np.random.normal(2, 4, size=85)
    print("p: {}".format(p), "\n")

    qT = np.multiply(N[24], N[71])[np.newaxis]
    print("qT: {}".format(qT), "\n")

    q = qT.T
    print("q: {}".format(q), "\n")

    f = findF(
        q=q,
        qT=qT,
        p=p
    )
    print("f: {}".format(f), "\n")

    g = findG(
        matrixM=M,
        matrixN=N,
        q=q,
        qT=qT,
        p=p
    )
    print("g: {}".format(g), "\n")


def main():
    initialConditions()


if __name__ == '__main__':
    main()
