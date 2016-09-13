# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda x: x.start)

        current_interval_index = 0
        next_interval_index = 1
        while(next_interval_index < len(intervals)):
            if intervals[current_interval_index].end> intervals[next_interval_index].start:
                return False
            else:
                current_interval_index += 1
                next_interval_index += 1
        return True
        