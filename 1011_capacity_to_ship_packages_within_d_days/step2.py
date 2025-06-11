from math import inf


class Solution1TLE:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_days_to_ship(capacity):
            days_to_ship = 0
            i = 0
            while i < len(weights):
                capacity_left = capacity
                days_to_ship += 1
                while i < len(weights) and capacity_left - weights[i] >= 0:
                    if weights[i] > capacity:
                        return inf
                    capacity_left -= weights[i]
                    i += 1
            return days_to_ship

        low = 1
        high = min_capacity = sum(weights)
        while low <= high:
            capacity = (low + high) // 2
            if get_days_to_ship(capacity) > days:
                low = capacity + 1
                continue
            min_capacity = min(min_capacity, capacity)
            high = capacity - 1
        return min_capacity


from math import inf


class Solution2AC:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_days_to_ship(capacity):
            days_to_ship = 0
            i = 0
            while i < len(weights):
                if weights[i] > capacity:
                    return inf
                capacity_left = capacity
                days_to_ship += 1
                while i < len(weights) and capacity_left - weights[i] >= 0:
                    capacity_left -= weights[i]
                    i += 1
            return days_to_ship

        low = 1
        high = min_capacity = sum(weights)
        while low <= high:
            capacity = (low + high) // 2
            print(f"low={low}, high={high}, cap={capacity}")
            if get_days_to_ship(capacity) > days:
                low = capacity + 1
                continue
            min_capacity = min(min_capacity, capacity)
            high = capacity - 1
        return min_capacity


class Solution3AC:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_days_to_ship(capacity):
            days_to_ship = 0
            i = 0
            while i < len(weights):
                capacity_left = capacity
                days_to_ship += 1
                while i < len(weights) and capacity_left - weights[i] >= 0:
                    capacity_left -= weights[i]
                    i += 1
            return days_to_ship

        low = max(weights)
        high = sum(weights)
        min_capacity = high
        while low <= high:
            capacity = (low + high) // 2
            print(f"low={low}, high={high}, cap={capacity}")
            if get_days_to_ship(capacity) > days:
                low = capacity + 1
                continue
            min_capacity = min(min_capacity, capacity)
            high = capacity - 1
        return min_capacity

class Solution4AC:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            days_to_ship = 0
            i = 0
            while i < len(weights):
                capacity_left = capacity
                days_to_ship += 1
                if days_to_ship > days:
                    return False
                while i < len(weights) and capacity_left - weights[i] >= 0:
                    capacity_left -= weights[i]
                    i += 1
            return True

        low = max(weights)
        high = sum(weights)
        min_capacity = high
        while low <= high:
            capacity = (low + high) // 2
            if not can_ship(capacity):
                low = capacity + 1
                continue
            min_capacity = min(min_capacity, capacity)
            high = capacity - 1
        return min_capacity
