class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1

# Solution1 の zero_index の命名を変えただけ
class Solution1_1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[non_zero_index] = nums[non_zero_index], nums[i]
                non_zero_index += 1



class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

# Erase–remove idiom / C++ remove を模倣した実装
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        val = 0 # target val to remove
        result = 0 # write index
        # first is read index
        for first in range(len(nums)):
            if nums[first] != val:
                nums[result] = nums[first]
                result += 1
        # Fill the rest by the target val...
        nums[result:] = [0] * (len(nums) - result)
