



# levenstain distance between two words
# if a[0]=b[0] lev(tail(a), tail(b))
# 1+min()

def lev(a, b):
    m = len(a)
    n = len(b)

    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    

    for i in range(m+1):
        matrix[0][i] = i

    for j in range(n+1):
        matrix[j][0] = j

    subCost = 0
    for j in range(1, m):
        for i in range(1, n):
            if a[j]==b[i]:
                subCost = 0
            else:
                subCost = 1

            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+subCost)
    return matrix[n-1][m-1]


print(lev("a", "acab"))