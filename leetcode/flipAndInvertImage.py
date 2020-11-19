def flip(A, index):
    if A[index] == 1:
        A[index] = 0
    else:
        A[index] = 1

def flipAndInvertImage(A):
    for i in range(len(A)):
        row = A[i]

        lo = 0
        hi = len(row) - 1

        while lo <= hi:
            temp = row[lo]
            row[lo] = row[hi]
            row[hi] = temp
            lo += 1
            hi -= 1

        for i in range(len(row)):
            flip(row, i)

    return A

A = [[1,1,0],[1,0,1],[0,0,0]]

print(flipAndInvertImage(A))

