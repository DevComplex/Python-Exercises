# https://leetcode.com/problems/container-with-most-water/

def max_area(height):
    l = 0
    r = len(height) - 1

    total_max_area = float('-inf')

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        total_max_area = max(area, total_max_area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return total_max_area