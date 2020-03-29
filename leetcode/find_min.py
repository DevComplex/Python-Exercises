# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def find_min(nums):
    N = len(nums)
    
    if N == 1 or nums[0] < nums[N - 1]:
        return nums[0]

    lo = 0
    hi = N - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid + 1] < nums[mid]:
            return nums[mid + 1]

        if nums[mid] < nums[mid - 1]:
            return nums[mid]

        if nums[mid] < nums[N - 1]:
            lo = mid + 1
        else:
            hi = mid - 1


print(find_min([5, 6, 7, 0, 1]))