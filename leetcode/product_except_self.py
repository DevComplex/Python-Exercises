# https://leetcode.com/problems/product-of-array-except-self/

def product_except_self(nums):
    N = len(nums)

    if N == 0 or N == 1:
        return nums

    left = [0] * N
    left[0] = nums[0]

    for i in range(N):
        if i > 0:
            left[i] = nums[i] * left[i - 1]

    right = [0] * N
    right[N - 1] = nums[N - 1]

    for i in reversed(range(N)):
        if i < N - 1:
            right[i] = nums[i] * right[i + 1]

    res = [0] * N

    for i in range(N):
        if i == 0:
            res[0] = right[1]
        elif i == N - 1:
            res[N - 1] = left[N - 2]
        else:
            res[i] = left[i - 1] * right[i + 1]

    return res

