def matrixOfSize(n):  # Macierz o stałym porzadku o wielkości n
    return [" ".join([f"{index*n + (j+1)}.{index*n + (j+1)}" for j in range(n)]) for index in range(n)]


def transposedMatrixOfSize(n):  # Transponowana wersja powyższego
    return [" ".join([f"{(index+1)+n*j}.{(index+1)+n*j}" for j in range(n)]) for index in range(n)]


# Transpozycja dowolnej macierzy o zadanej postaci
def transpose(matrix):
    return [" ".join([line.split() for line in matrix][j][i] for j in range(len(matrix))) for i in range(len(matrix))]


#matrix = matrixOfSize(5)
matrix = transposedMatrixOfSize(3)
print(matrix)
print(transpose(matrix))
