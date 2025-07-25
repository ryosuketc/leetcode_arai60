# Wrong answer
class Solution1WA:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_days_to_ship(capacity):
            days_to_ship = 1
            remaining_capacity = capacity
            for weight in weights:
                if remaining_capacity - weight > 0:
                    remaining_capacity -= weight
                else:
                    remaining_capacity = capacity - weight
                    days_to_ship += 1
            return days_to_ship

        low = 1
        high = min_capacity = sum(weights)
        while low <= high:
            capacity = (low + high) // 2
            if get_days_to_ship(capacity) <= days:
                min_capacity = min(min_capacity, capacity)
                high = capacity - 1
            else:
                low = capacity + 1
        return min_capacity


from math import inf


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def get_days_to_ship(capacity):
            days_to_ship = 1
            remaining_capacity = capacity
            for weight in weights:
                if weight > capacity:
                    return inf
                if remaining_capacity - weight >= 0:
                    remaining_capacity -= weight
                else:
                    remaining_capacity = capacity - weight
                    days_to_ship += 1
            return days_to_ship

        low = 1
        high = min_capacity = sum(weights)
        while low <= high:
            capacity = (low + high) // 2
            # print(f"low={low}, high={high}, cap={capacity}")
            if get_days_to_ship(capacity) <= days:
                min_capacity = min(min_capacity, capacity)
                high = capacity - 1
            else:
                low = capacity + 1
        return min_capacity

