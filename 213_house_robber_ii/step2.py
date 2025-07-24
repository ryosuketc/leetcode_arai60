class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 1:
            return nums[0]
        
        def rob_helper(houses):
            if not houses:
                return 0
            if len(houses) <= 1:
                return houses[0]
            skipped_last = houses[0]
            robbed_last = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                max_amount = max(skipped_last + houses[i], robbed_last)
                skipped_last = robbed_last
                robbed_last = max_amount
            return robbed_last
        
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))
