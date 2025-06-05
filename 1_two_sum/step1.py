class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared_numbers = {nums[0]: 0}
        for i in range(1, len(nums)):
            if target - nums[i] in appeared_numbers:
                return [i, appeared_numbers[target - nums[i]]]
            appeared_numbers[nums[i]] = i
        return [-1, -1]