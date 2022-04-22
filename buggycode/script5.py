# Program to multiply two matrices using nested loops
from pprint import pprint
import numpy as np


def create_result_matrix_size(row, cols):
    result = []
    for i in range(row):
        result.append([])
        for j in range(cols):
            result[i].append(0)
    return result


def matrix_multiplication(X, Y):
    # iterate through rows of X
    result = create_result_matrix_size(len(X), len(Y[0]))
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y)):
            # iterate through rows of Y
            for k in range(len(X)):
                result[i][j] += X[i][k] * Y[k][j]
            
    return result


def main():
    # 2x3 matrix
    a = [[12,7,3],
        [4 ,5,6]]

    # 3x3 matrix
    b = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]

    result = matrix_multiplication(a, b)
    print("Result of matrix multiplication is:")
    pprint(np.array(result))
    print("Should be:")
    pprint(np.array(a) @ np.array(b))

if __name__ == "__main__":
    main()