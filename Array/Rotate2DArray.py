def rotateMatrix(matrix):
    n = len(matrix)
    for i in range(len(matrix)//2):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
            matrix[j][n-i-1] = temp
    
    return matrix

# Improve syntax
def rotateMatrix2(matrix):
    n = len(matrix)
    for i in range(len(matrix)//2):
        for j in range(i, n-i-1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[~j][i]
            matrix[~j][i] = matrix[~i][~j]
            matrix[~i][~j] = matrix[j][~i]
            matrix[j][~i] = temp
    
    return matrix

print(rotateMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))