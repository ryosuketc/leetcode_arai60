class SolutionWA:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        max_money = 0
        # Max amount of money obtained by robbing the house in each index.
        max_money_rob_house = [0] * len(nums)
        max_money_rob_house[0] = nums[0]
        max_money_rob_house[1] = nums[1]
        for house in range(2, len(nums)):
            # When robbing the current house, the previous house cannot be robbed.
            rob_house = nums[house] + max_money_rob_house[house - 2]
            not_rob_house = dp[house - 1]
            max_money = max(max_money, rob_house, not_rob_house)
            max_money_rob_house[house] = rob_house
        return max_money


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        # Max amount of money obtained by robbing the house in each index.
        max_money = [0] * len(nums)
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        for house in range(2, len(nums)):
            rob_house = nums[house] + max_money[house - 2]
            not_rob_house = max_money[house - 1]
            max_money[house] = max(rob_house, not_rob_house)
        return max_money[-1]
