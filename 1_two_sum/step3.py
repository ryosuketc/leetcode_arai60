class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        existing_nums_to_index = {nums[0]: 0}

        for i in range(1, len(nums)):
            num = nums[i]
            complement = target - num
            if complement in existing_nums_to_index:
                return [existing_nums_to_index[complement], i]
            existing_nums_to_index[num] = i
        
        return [] # Should be unreachable.


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared_nums_to_index = {nums[0]: 0}
        for i in range(1, len(nums)):
            num = nums[i]
            complement = target - num
            if complement in appeared_nums_to_index:
                return [appeared_nums_to_index[complement], i]
            appeared_nums_to_index[num] = i
        return []
