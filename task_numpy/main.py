import numpy as np


def initMatrix():
    N = 85

    matrixM_diag = [i * 2 + 1 for i in range(1, N + 1)]
    matrixM = np.diag(np.array(matrixM_diag))
    matrixM[(matrixM == 0)] = 2
    print(matrixM)

    matrixN = np.zeros((N, N))
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
    print(matrixN)


def main():
    initMatrix()


if __name__ == '__main__':
    main()
