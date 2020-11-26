def twoSum(nums, target):
    h = {}

    for i, num in enumerate(nums):
        newTarget = target - num
        
        if newTarget in h:
            return [h[newTarget], i]

        h[num] = i

    return -1