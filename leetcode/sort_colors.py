# https://leetcode.com/problems/sort-colors/

def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp

def sort_colors(colors):
    N = len(colors)

    left = 0

    for i in range(N):
        if colors[i] == 0:
            swap(colors, i, left)
            left += 1

    right = N - 1

    for i in reversed(range(N)):
        if colors[i] == 0:
            break

        if colors[i] == 2:
            swap(colors, i, right)
            right -= 1