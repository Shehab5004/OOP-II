def add_matrices(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result
print("Enter dimensions of the matrices (rows columns):")
rows, cols = map(int, input().split())
print("Enter elements of the first matrix:")
matrix_a = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix_a.append(row)
print("Enter elements of the second matrix:")
matrix_b = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix_b.append(row)
result_matrix = add_matrices(matrix_a, matrix_b)
print("The sum of the two matrices is:")
for row in result_matrix:
    print(" ".join(map(str, row)))
