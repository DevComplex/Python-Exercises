# https://leetcode.com/problems/meeting-rooms/

def can_attend_meetings(intervals):
    intervals.sort(key=(lambda x: x[0]))

    for i in range(0, len(intervals) - 1):
        if intervals[i + 1][0] <= intervals[i][1]:
            return False

    return True