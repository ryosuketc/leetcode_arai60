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

        occupied_rooms = 0 # currently used
        required_rooms = 0 # min number of rooms required
        for time, time_type in times:
            if time_type == START:
                occupied_rooms += 1
            else: # END
                occupied_rooms -= 1
            required_rooms = max(required_rooms, occupied_rooms)
        return required_rooms
