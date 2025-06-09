class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            middle_value = nums[middle_index]
            if middle_value == target:
                return middle_index
            elif middle_value < target:
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
        return left_index
