class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals)
        last_end_time = -1 # Earlier than any other meetings
        for start_time, end_time in sorted_intervals:
            if start_time < last_end_time:
                return False
            last_end_time = end_time
        return True
