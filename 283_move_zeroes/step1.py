class Solution1WA:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = len(nums) - 1
        for i, num in enumerate(nums):
            if num == 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index -= 1


class Solution2WA:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i, num in enumerate(nums):
            if num == 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1


class Solution3AC:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1
