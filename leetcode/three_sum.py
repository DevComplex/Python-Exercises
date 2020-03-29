# https://leetcode.com/problems/3sum/

def three_sum(nums, target):
    output = []
    N = len(nums)

    if N < 3:
        return output

    nums.sort()

    for i in range(N - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = N - 1

        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]

            if curr_sum == target:
                triplet = [nums[i], nums[l], nums[r]]
                output.append(triplet)

                l += 1
                r -= 1

                while l < r and nums[l] == nums[l - 1]:
                    l += 1

                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif curr_sum > target:
                r -= 1
            else:
                l += 1

    return output