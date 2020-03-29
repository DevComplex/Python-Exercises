# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
    seen_nums = {}

    for index, num in enumerate(nums):
        new_target = target - num

        if new_target in seen_nums:
            return [seen_nums[new_target], index]

        seen_nums[num] = index

    return None