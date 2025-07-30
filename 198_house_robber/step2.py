class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        two_previous_max = nums[0]
        previous_max = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_money = max(two_previous_max + nums[i], previous_max)
            two_previous_max = previous_max
            previous_max = max_money
        return previous_max


class Solution2:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        two_previous_max = 0
        previous_max = 0
        for num in nums:
            max_money = max(two_previous_max + num, previous_max)
            two_previous_max = previous_max
            previous_max = max_money
        return previous_max


class Solution3:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def get_max_value(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]
            
            max_money = max(nums[i] + get_max_value(i - 2), get_max_value(i - 1))
            memo[i] = max_money
            return memo[i]

        return get_max_value(len(nums) - 1)
