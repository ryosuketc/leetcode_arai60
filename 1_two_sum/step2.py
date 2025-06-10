class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared_nums_to_index = {nums[0]: 0}

        for i in range(1, len(nums)):
            num = nums[i]
            complement = target - num
            if complement in appeared_nums_to_index:
                return [i, appeared_nums_to_index[complement]]
            appeared_nums_to_index[num] = i
        return [-1, -1]
