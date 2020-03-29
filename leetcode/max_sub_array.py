# https://leetcode.com/problems/maximum-subarray/

def max_sub_array(nums):
    total_max = nums[0]
    local_max = nums[0]

    for i in range(1, len(nums)):
        local_max = max(nums[i], nums[i] + local_max)
        total_max = max(total_max, local_max)

    return total_max