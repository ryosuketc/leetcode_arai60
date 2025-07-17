class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(houses):
            if not houses:
                return 0
            if len(houses) <= 1:
                return houses[0]
            max_amounts = [0] * len(houses)
            max_amounts[0] = houses[0]
            max_amounts[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                max_amounts[i] = max(houses[i] + max_amounts[i - 2], max_amounts[i - 1])
            return max_amounts[-1]
        
        if not nums:
            return 0
        if len(nums) <= 1:
            return nums[0]
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))
