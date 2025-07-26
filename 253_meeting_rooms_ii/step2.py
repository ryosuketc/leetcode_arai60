class Solution1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        rooms = 0
        start_times = sorted([interval[0] for interval in intervals])
        end_times = sorted([interval[1] for interval in intervals])
        e_ptr = 0
        for s_ptr in range(len(intervals)):
            rooms += 1
            if end_times[e_ptr] <= start_times[s_ptr]:
                rooms -= 1
                e_ptr += 1
        return rooms


class Solution1_1:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        start_times = []
        end_times = []
        for start_time, end_time in intervals:
            start_times.append(start_time)
            end_times.append(end_time)
        start_times.sort()
        end_times.sort()

        num_ongoing_meetings = 0
        end_index = 0
        for start_index in range(len(start_times)):
            num_ongoing_meetings += 1
            if end_times[end_index] <= start_times[start_index]:
                num_ongoing_meetings -= 1
                end_index += 1
        return num_ongoing_meetings


# Used as delta. When start, rooms need to be incremented vs. end -> decremented.
START = 1
END = -1


class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # A list of (time, delta), where delta is either START or END (increment or decrement).
        times = []
        for start_time, end_time in intervals:
            times.append((start_time, START))
            times.append((end_time, END))
        times.sort()

        num_ongoing_meetings = 0
        max_required_rooms = 0
        for _, delta in times:
            num_ongoing_meetings += delta
            max_required_rooms = max(max_required_rooms, num_ongoing_meetings)
        return max_required_rooms



from heapq import heappop, heappush


class Solution3:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        num_ongoing_meetings = 0
        max_required_rooms = 0
        ongoing_meeting_end_times = []
        for start_time, end_time in sorted(intervals):
            num_ongoing_meetings += 1
            heappush(ongoing_meeting_end_times, end_time)
            while ongoing_meeting_end_times[0] <= start_time:
                heappop(ongoing_meeting_end_times)
                num_ongoing_meetings -= 1
            max_required_rooms = max(max_required_rooms, num_ongoing_meetings)
        return max_required_rooms


