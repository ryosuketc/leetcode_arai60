# When the same time is given, end should be processed first.
START = 0
END = -1


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # A list of (time, time_type), where time_type is either START or END.
        times = []
        for start_time, end_time in intervals:
            times.append((start_time, START))
            times.append((end_time, END))
        times.sort()

        num_ongoing_meetings = 0
        max_required_rooms = 0
        for _, time_type in times:
            if time_type == START:
                num_ongoing_meetings += 1
            else:
                num_ongoing_meetings -= 1
            max_required_rooms = max(max_required_rooms, num_ongoing_meetings)
        return max_required_rooms
