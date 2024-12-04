def multiply_matrices(mat1, mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    cols2 = len(mat2[0])

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):  
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result

print("Enter dimensions of the first matrix (rows columns):")
rows1, cols1 = map(int, input().split())

print("Enter elements of the first matrix:")
matrix_a = []
for i in range(rows1):
    row = list(map(int, input().split()))
    matrix_a.append(row)

print("Enter dimensions of the second matrix (columns must match rows of the first):")
cols2 = int(input("Columns: "))

print("Enter elements of the second matrix:")
matrix_b = []
for i in range(cols1):
    row = list(map(int, input().split()))
    matrix_b.append(row)

result_matrix = multiply_matrices(matrix_a, matrix_b)

print("The product of the two matrices is:")
for row in result_matrix:
    print(" ".join(map(str, row)))
