#Primero defino mi matriz y el vector de soluciones en base a la ecuacion dada

matrix = [[4, 1, 2, -1],
          [3, -1, 0, 2],
          [2, 2, 4, -1],
          [1, -1, -1, 3]]

solutions = [20, 8, 16, 6]

#Aquí el codigo de Matriz por Dolittle
def dolittle(matrix, solutions):
    # Tamaño de la matriz
    n = len(matrix)

    # Inicializo aquí las matrices L y U
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    # Descomposición de la matriz en L y U
    for i in range(n):
        # Elementos de la diagonal de L
        L[i][i] = 1.0

        # Elementos de la diagonal de U y por encima de la diagonal
        for j in range(i, n):
            sum_lu = sum(L[i][k]*U[k][j] for k in range(i))
            U[i][j] = matrix[i][j] - sum_lu

        # Elementos por debajo de la diagonal de L
        for j in range(i+1, n):
            sum_lu = sum(L[j][k]*U[k][i] for k in range(i))
            L[j][i] = (matrix[j][i] - sum_lu) / U[i][i]

    # Resolver el sistema de ecuaciones dado
    # Primero, resolver L*y = b por sustitución hacia adelante
    y = [0.0] * n
    for i in range(n):
        y[i] = solutions[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]

    # Luego, resolver U*x = y por sustitución hacia atrás
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x
#Esta función lo que hace es una descomposición de la matriz en L y U utilizando
# el método de Dolittle y luego resuelve el sistema de ecuaciones utilizando
# sustitución hacia adelante y hacia atrás.

#Por ultimo digo que imprima la solucion de la funciom Dolittle
result = dolittle(matrix, solutions)
print(result)

#Fin :)
