# https://leetcode.com/problems/insert-interval/

def overlaps(a, b):
    x, y = sorted([a, b], key=(lambda x : x[0]))
    return y[0] <= x[1]

def merge(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]

def comes_before(a, b):
    return a[1] < b[0]

def comes_after(a, b):
    return a[0] > b[1]

def insert_interval(intervals, new_interval):
    has_new_interval = True

    if comes_before(new_interval, intervals[0]):
        intervals = [new_interval] + intervals
        has_new_interval = False
    elif comes_after(new_interval, intervals[len(intervals) - 1]):
        intervals = intervals + [new_interval]
        has_new_interval = False

    curr_interval = intervals[0]

    merged_intervals = []

    for i in range(1, len(intervals)):
        next_interval = intervals[i]

        if has_new_interval:
            if overlaps(curr_interval, new_interval):
                curr_interval = merge(curr_interval, new_interval)
                has_new_interval = False
            elif overlaps(new_interval, next_interval):
                merged_intervals.append(curr_interval)
                curr_interval = merge(new_interval, next_interval)
                has_new_interval = False
                continue
            elif comes_before(new_interval, next_interval):
                merged_intervals.append(curr_interval)
                merged_intervals.append(new_interval)
                curr_interval = next_interval
                has_new_interval = False
                continue

        if overlaps(curr_interval, next_interval):
            curr_interval = merge(curr_interval, next_interval)
        else:
            merged_intervals.append(curr_interval)
            curr_interval = next_interval

    merged_intervals.append(curr_interval)

    return merged_intervals