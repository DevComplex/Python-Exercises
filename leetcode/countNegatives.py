grid = [[1,-1],[-1,-1]]

def binarySearch(arr):
    if len(arr) == 1 and arr[0] < 0:
        return 0

    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid > 0 and arr[mid] < 0 and arr[mid - 1] > 0:
            return mid
        if mid < len(arr) - 1 and arr[mid] > 0 and arr[mid + 1] < 0:
            return mid + 1
        if arr[mid] < 0:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo if lo < len(arr) else -1

def countNegatives(grid):
    rows = len(grid)
    cols = len(grid[0])

    count = 0

    for row in grid:
        index = binarySearch(row)

        if index != -1:
            count += cols - index

    return count

result = countNegatives(grid)

print(result)