import collections
from functools import cmp_to_key


def frequencySort(nums):
    count = collections.Counter(nums)
    
    def freqCmp(a, b):
        if count[a] == count[b]:
            return b - a

        return count[a] - count[b]

    nums.sort(key=cmp_to_key(freqCmp))

    return nums

nums = [-1,1,-6,4,5,-6,1,4,1]

print(frequencySort(nums))
