# Given a two-dimensional array, if any element within is zero, 
# make its whole row and column zero. Consider the matrix below.

#O(M*N)

def zeroOut(arr):
    rows = len(arr) 
    columns = len(arr[0])

    zeroRow = [] 
    zeroCol = []

    for r in range(rows): 
        for c in range(columns): 
            if arr[r][c] == 0: 
                zeroRow.append(r) 
                zeroCol.append(c) 
    
    for r in range(rows): 
        for c in range(columns): 
            if r in zeroRow or c in zeroCol:
                arr[r][c] = 0


    return arr

print(zeroOut([[0, 1, 3, 4], [1, 2, 3, 4]]))