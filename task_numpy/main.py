import numpy as np

countN = 85


def initMatrix():
    matrixM_diag = [i * 2 + 1 for i in range(1, countN + 1)]
    matrixM = np.diag(np.array(matrixM_diag))
    matrixM[(matrixM == 0)] = 2

    matrixN = np.zeros((countN, countN))
    matrixN_row_even = [4, 4, 5]
    matrixN_row_odd = [4, 7]
    for indexR, row in enumerate(matrixN):
        for indexC, column in enumerate(row):
            # Четная(even) строка
            if indexR % 2 == 0:
                pos = indexC % len(matrixN_row_even)
                matrixN[indexR, indexC] = matrixN_row_even[pos]

            # Нечетная(odd) строка
            else:
                pos = indexC % len(matrixN_row_odd)
                matrixN[indexR, indexC] = matrixN_row_odd[pos]
    return matrixM, matrixN


def pSet(arr, i):
    if i < countN:
        arr = np.append(arr, 1 + np.random.normal(2, 4))
        i += 1
        arr = pSet(arr, i)
    return arr


def qSet(arr, j, matrixN):
    if j < countN:
        arr = np.append(arr, np.multiply(matrixN[24, j], matrixN[71, j]))
        j += 1
        arr = qSet(arr, j, matrixN)
    return arr


def findF(q, qT, p):
    multQ = np.dot(q, qT)

    f = np.linalg.det(multQ)

    result = np.dot(f, p)
    return result


def sumG(matrixM, matrixN, multQ, i, arr):
    if i < countN:
        _sum = matrixM[i, i] - matrixN[i, i] + multQ

        arr = np.append(arr, _sum)
        i += 1
        arr = sumG(matrixM, matrixN, multQ, i, arr)
    return arr


def findG(matrixM, matrixN, q, qT, p):
    multQ = np.dot(qT, q)

    _set = sumG(matrixM, matrixN, multQ, 0, np.array([]))

    result = np.linalg.norm(_set, 2)

    return result


def initialConditions():
    M, N = initMatrix()
    print("M = {}".format(M), "\n")
    print("N = {}".format(N), "\n")

    p = pSet(arr=np.array([]), i=0)
    print("p = {}".format(p), "\n")

    qT = qSet(arr=np.array([]), j=0, matrixN=N)[np.newaxis]
    print("qT = {}".format(qT), "\n")
    q = qT.T
    print("q = {}".format(q), "\n")

    resultF = findF(q, qT, p)
    print("f = {}".format(resultF), "\n")

    resultG = findG(
        matrixM=M,
        matrixN=N,
        q=q,
        qT=qT,
        p=p
    )
    print("g = {}".format(resultG), "\n")


def main():
    initialConditions()


if __name__ == '__main__':
    main()
