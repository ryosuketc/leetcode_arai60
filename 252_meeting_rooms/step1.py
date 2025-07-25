class Solution1:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        sorted_intervals = sorted(intervals)
        previous_end_time = sorted_intervals[0][1]
        for i in range(1, len(sorted_intervals)):
            start_time, end_time = sorted_intervals[i]
            if start_time < previous_end_time:
                return False
            previous_end_time = max(previous_end_time, end_time)
        return True


class Solution2:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) <= 1:
            return True
        sorted_intervals = sorted(intervals)
        for i in range(1, len(sorted_intervals)):
            start_time, end_time = sorted_intervals[i]
            previous_end_time = sorted_intervals[i - 1][1]
            if start_time < previous_end_time:
                return False
        return True

