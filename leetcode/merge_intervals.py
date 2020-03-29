# https://leetcode.com/problems/merge-intervals/

def merge_intervals(intervals):
    intervals.sort(key=(lambda x: x[0]))
    merged_intervals = []

    curr_interval = intervals[0]

    for i in range(1, len(intervals)):
        next_interval = intervals[i]

        if next_interval[0] <= curr_interval[1]:
            curr_interval = [curr_interval[0], max(curr_interval[1], next_interval[1])]
        else:
            merged_intervals.append(curr_interval)
            curr_interval = next_interval
    
    merged_intervals.append(curr_interval)
    return merged_intervals