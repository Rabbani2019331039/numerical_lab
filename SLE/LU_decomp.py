## module LUpivot
''' a,seq = LUdecomp(a,tol=1.0e-9).
LU decomposition of matrix [a] using scaled row pivoting.
The returned matrix [a] = contains [U] in the upper
triangle and the nondiagonal terms of [L] in the lower triangle.
Note that [L][U] is a row-wise permutation of the original [a];
the permutations are recorded in the vector {seq}.

x = LUsolve(a,b,seq).
Solves [L][U]{x} = {b}, where the matrix [a] = and the
permutation vector {seq} are returned from LUdecomp.
'''
import numpy as np

def LUdecomp(a,tol=1.0e-9):
    n = len(a)
    seq = np.array(range(n))

    # Set up scale factors
    # s = np.zeros((n))
    # for i in range(n):
    #     s[i] = max(abs(a[i,:]))

    for k in range(0,n-1):
        # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam

    return a

def LUsolve(a,b):
    n = len(a)

    # Rearrange constant vector; store it in [x]
    x = b.copy()  

    # Solution
    for k in range(1,n):
        x[k] = x[k] - np.dot(a[k, 0:k],x[0:k])

    x[n-1] = x[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        x[k] = (x[k] - np.dot(a[k,k+1:n],x[k+1:n]))/a[k,k]

    return x

def matInv(a):
    n = len(a[0])
    aInv = np.identity(n)
    a = LUdecomp(a)
    for i in range(n):
        aInv[:,i] = LUsolve(a, aInv[:, i])
    return aInv


# a = np.array([[25.0, 5.0, 1.0], [64.0, 8.0, 1.0], [144.0, 12.0, 1.0]])
# b = np.array([106.8, 177.2, 279.2])


# x = matInv(a)
# print(x)

