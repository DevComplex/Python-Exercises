# https://leetcode.com/problems/maximum-product-subarray/

def max_product(nums):
    pos_prod = nums[0]
    neg_prod = nums[0]
    max_prod = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            temp = pos_prod
            pos_prod = neg_prod
            neg_prod = temp

        pos_prod = max(nums[i], pos_prod * nums[i])
        neg_prod = min(nums[i], neg_prod * nums[i])
        max_prod = max(max_prod, pos_prod)

    return max_prod