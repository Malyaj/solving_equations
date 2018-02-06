# -*- coding: utf-8 -*-
"""
Solving a system of linear equations - Gaussian Elimination
"""


def print_matrix(mat):
    """assumes that mat is a square matrix"""
    n = len(mat)
    for row in range(n):
        print(mat[row])
    print("-+-" * 25)


def augmented_matrix(A, b):
    """returns the augmented matrix,
    assuming A is a square matrix"""
    aug, n = [], len(A)
    for i in range(n):
        t = A[i]
        t.append(b[i])
        aug.append(t)
    return aug


# example data, will add input functionality later
r1 = [5, -4, 2]
r2 = [2, 3, -1]
r3 = [1, 1, 1]

A = [r1, r2, r3]
b = [3, 4, 3]

# augmented matrix
A_b = augmented_matrix(A, b)


n = len(A)


# traversing column-wise , collecting factors to make the lower-triangular elements zero
for c_iter in range(n):
    #print_matrix(A)
    m = []
    for row in range(n):
        if row <= c_iter:
            m.append(0)
        else:
            m.append(-1 * A_b[row][c_iter] / A_b[c_iter][c_iter])
    for row in range(n):
        for col in range(n+1):
            A_b[row][col] += m[row] * A_b[c_iter][col]
    #print_matrix(A)
""" backpropagation : transforming the matrix A into an identity matrix will
give the solution as b"""
print_matrix(A_b)


#for row in range(n-1,-1, -1):
#    d = A[row][row]
#    for col in range(n+1):
#        A[row][col] /= d
#        A[row-1][col]
for row in range(n-1, 0,-1):
    d = A_b[row][row]
    for col in range(n+1):
        A_b[row][col] /= d
    m = []
    for col in range(n+1):
        if row <= col and A_b[row][col] != 0:
            m.append(-1 * A_b[row-1][col] / A_b[row][col])
        else:
            m.append(0)
    for col in range(n+1):
        A_b[row-1][col] += m[col]

print_matrix(A_b)
    