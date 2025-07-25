class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 1:
            return nums[0]
        
        max_amounts = [0] * len(nums)
        max_amounts[0] = nums[0]
        max_amounts[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_amounts[i] = max(nums[i] + max_amounts[i - 2], max_amounts[i - 1])
        return max_amounts[-1]
