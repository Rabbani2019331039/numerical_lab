## module gaussPivot
''' x = gaussPivot(a,b,tol=1.0e-12).
Solves [a]{x} = {b} by Gauss elimination with
scaled row pivoting
'''
import numpy as np

# import error
def gaussPivot(a,b,tol=1.0e-12):
    n = len(b)

    for k in range(0,n-1):
    # Row interchange, if needed
        p = np.argmax(np.abs(a[k:n,k])) + k
        # if abs(a[p,k]) < tol: error.err('Matrix is singular')
        if p != k:
            b[[k,p]] = b[[p,k]]
            a[[k,p]] = a[[p,k]]


    # Elimination
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    # if abs(a[n-1,n-1]) < tol: error.err('Matrix is singular')

    # Back substitution
    b[n-1] = b[n-1]/a[n-1,n-1]
    for k in range(n-2,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]

    return b

# a = np.array([[144.0, 12.0, 1.0], [64.0, 8.0, 1.0], [25.0, 5.0, 1.0]])
# b = np.array([279.2, 177.2, 106.8])

# c = gaussPivot(a,b)

# print(c)