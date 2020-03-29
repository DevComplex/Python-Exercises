# https://leetcode.com/problems/meeting-rooms-ii/ 

import heapq

def min_meeting_rooms(intervals):
    intervals.sort(key=(lambda x: x[0]))

    min_heap = []

    for start, end in intervals:
        if len(min_heap) == 0:
            heapq.heappush(min_heap, end)
            continue
        elif start >= min_heap[0]:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap, end)

    return len(min_heap)