import numpy as np

def gauss_jordan(A, b):

    A = A.astype(float)
    
  
    Ab = np.hstack([A, b.reshape(-1, 1)])
    n = len(b)


    for i in range(n):
        Ab[i] = Ab[i] / Ab[i, i]
        for j in range(n):
            if i != j:
                Ab[j] = Ab[j] - Ab[i] * Ab[j, i]

    x = Ab[:, -1]
    return x


A = np.array([[2, 3, -4], [4, 7, 5], [1, 1, 3]])
b = np.array([5, 6, 7])
resultado = gauss_jordan(A, b)
print("La solución es:", resultado)

