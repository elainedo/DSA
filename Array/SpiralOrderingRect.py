def spiralordering(matrix):
    rowBeg = 0
    rowEnd = len(matrix)-1
    colBeg = 0
    colEnd = len(matrix[0])-1 if len(matrix) >0 else 0
    result = []
    matrix_size = (rowEnd+1)*(colEnd+1)
    
    while (rowBeg <= rowEnd and colBeg <= colEnd):
        for col in range(colBeg, colEnd+1):
            if len(result) < matrix_size:
                result.append(matrix[rowBeg][col])

        for row in range(rowBeg+1, rowEnd):
            if len(result) < matrix_size:
                result.append(matrix[row][colEnd])

        for col in range(colEnd, colBeg-1, -1):
            if len(result) < matrix_size:
                result.append(matrix[rowEnd][col])

        for row in range(rowEnd-1, rowBeg, -1):
            if len(result) < matrix_size:
                result.append(matrix[row][colBeg])

        rowBeg+=1
        rowEnd-=1
        colBeg+=1
        colEnd-=1

    return result

print(spiralordering([[1,2,3],[4,5,6],[7,8,9]]))
# 1, 2, 3, 6, 9, 8, 7, 4, 5

print(spiralordering([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
# 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10

print(spiralordering([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]