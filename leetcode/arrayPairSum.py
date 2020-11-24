def arrayPairSum(nums):
    nums.sort()

    i = 0
    total = 0

    while i < len(nums) - 1:
        total += min(nums[i], nums[i + 1])
        i += 2

    return total

nums = [6,2,6,5,1,2]

print(arrayPairSum(nums))
