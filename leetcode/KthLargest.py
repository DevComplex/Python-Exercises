import heapq

class KthLargest(object):
    def add(self, num):
        if len(self.storage) < self.k:
            heapq.heappush(self.storage, num)
        elif num > self.storage[0]:
            heapq.heappop(self.storage)
            heapq.heappush(self.storage, num)

        return self.storage[0]

    def __init__(self, k, nums):
        self.storage = []
        self.k = k

        for num in nums:
            self.add(num)