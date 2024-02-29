import numpy as np


def recursive(n):
    if n <= 1:
        return n
    return recursive(n-1) + recursive(n-2)


def iterative(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


def dynamic(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]


def matrix(n):

    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):

    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


def power(F, n):

    if (n == 0 or n == 1):
        return
    M = [[1, 1],
         [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if (n % 2 != 0):
        multiply(F, M)


def binet(n):
    phi = (1 + 5**0.5) / 2
    psi = (1 - 5**0.5) / 2
    return int((phi**n - psi**n) / 5**0.5)


def eig_k(eig_val, k):
    return eig_val**k


def u_k(eig_val,s_inv, u_0, k, s):
    return s * eig_k(eig_val,k) * s_inv * u_0


def eigen_vector_method(n):
    phi = (1 + 5**0.5) / 2
    psi = (1 - 5**0.5) / 2
    a = np.matrix([[1,      1],      [1,  0]])
    s = np.matrix([[phi, psi], [1,  1]])
    s_inv = np.matrix([[1,     -psi], [-1, phi]]) * (1/np.sqrt(5))
    eig_val = np.matrix([[phi, 0],      [0,  psi]])
    u_0 = np.matrix([[1],              [0]])
    f_n= u_k(eig_val,s_inv, u_0, n, s)
    return int(round(f_n[0,0]))