def merge(nums1, m, nums2, n):
    curr = m + n - 1
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[curr] = nums1[m]
            m -= 1
        else:
            nums1[curr] = nums2[n]
            n -= 1
        
        curr -= 1

    while m >= 0:
        nums1[curr] = nums1[m]
        curr -= 1
        m -= 1

    while n >= 0:
        nums1[curr] = nums2[n]
        curr -= 1
        n -= 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)

print(nums1)