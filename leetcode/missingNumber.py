def missingNumber(nums):
    realTotal = (len(nums) * (len(nums) + 1)) // 2
    total = sum(nums)
    return realTotal - total