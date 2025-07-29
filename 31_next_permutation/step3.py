class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j) -> None:
            nums[i], nums[j] = nums[j], nums[i]

        def rfind_first_not_descending() -> int:
            for i in reversed(range(len(nums) - 1)):
                if nums[i] < nums[i + 1]:
                    return i
            return -1
        
        def rfind_first_greater_than(target: int) -> int:
            for i in reversed(range(len(nums))):
                 if nums[i] > target:
                    return i
            # Unreachable
        
        def reverse_in_range(start: int, end : int = len(nums) - 1) -> None:
            while start < end:
                swap(start, end)
                start += 1
                end -= 1
        
        pivot_index = rfind_first_not_descending()
        if pivot_index == -1:
            nums.reverse()
            return
        swap_index = rfind_first_greater_than(nums[pivot_index])
        swap(pivot_index, swap_index)
        reverse_in_range(pivot_index + 1)
