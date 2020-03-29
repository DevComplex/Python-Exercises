# https://leetcode.com/problems/contains-duplicate/

def contains_duplicate(num):
    return len(set(num)) != len(num)