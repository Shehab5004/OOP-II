def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed
print("Enter dimensions of the matrix (rows columns):")
rows, cols = map(int, input().split())

print("Enter elements of the matrix:")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
transposed_matrix = transpose_matrix(matrix)
print("The transposed matrix is:")
for row in transposed_matrix:
    print(" ".join(map(str, row)))
