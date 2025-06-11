class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship_in_days(capacity):
            days_to_ship = 1
            capacity_left = capacity
            for weight in weights:
                if capacity_left - weight >= 0:
                    capacity_left -= weight
                    continue
                capacity_left = capacity
                capacity_left -= weight
                days_to_ship += 1
                if days_to_ship > days:
                    return False
            return True

        low = max(weights)
        high = sum(weights)
        min_capacity = high
        while low <= high:
            capacity = (low + high) // 2
            if can_ship_in_days(capacity):
                min_capacity = min(min_capacity, capacity)
                high = capacity - 1
                continue
            low = capacity + 1
        return min_capacity
            
