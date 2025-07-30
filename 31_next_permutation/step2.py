class Solution1:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i: int, j: int) -> None:
            nums[i], nums[j] = nums[j], nums[i]

        def find_first_not_decending_from_last() -> int:
            for i in reversed(range(len(nums) - 1)):
                if nums[i] < nums[i + 1]:
                    return i
            return -1
        
        def find_first_greater(target) -> int:
            for i in reversed(range(len(nums))):
                if nums[i] > target:
                    return i

        def reverse_after(start: int):
            end = len(nums) - 1
            while start < end:
                swap(start, end)
                start += 1
                end -= 1

        left = find_first_not_decending_from_last()
        if left == -1:
            nums.reverse()
            return
        right = find_first_greater(nums[left])
        swap(left, right)
        reverse_after(left + 1)


class Solution2:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i: int, j: int) -> None:
            nums[i], nums[j] = nums[j], nums[i]

        def rfind_first_not_descending() -> int:
            # NOTE: If the entire num is asceding order, the next perm is nums with the last two elements are swapped.
            # For that purpose, this function returns `len(nums) - 2` for such nums,
            # while such behavior may conflict wiht the function name of `rfind_first_not_descending`.
            # pivot_index = len(nums) - 2 and swap_index = len(nums) - 1, resulting in the two being swapped byt he outer nextPermutation function.
            for i in reversed(range(len(nums) - 1)):
                if nums[i] < nums[i + 1]:
                    return i
            # The entire nums is in descending order.
            return -1

        def rfind_first_greater_than(target: int) -> int:
            for i in reversed(range(len(nums))):
                if nums[i] > target:
                    return i
            # Unreachable - this function is supposed to return some int, not None.
        
        def reverse_in_range(start: int, end : int = len(nums) - 1) -> None:
            while start < end:
                swap(start, end)
                start += 1
                end -= 1

        # def reverse_in_range2(start: int, end : int = len(nums)) -> None:
        #     end = end - 1 # Make end not inclusive to be consistent with the built-in `range`.
        #     while start < end:
        #         swap(start, end)
        #         start += 1
        #         end -= 1

        pivot_index = rfind_first_not_descending()
        # The entire nums is in descending order -> ascending order is the next perm.
        if pivot_index == -1:
            nums.reverse()
            return
        swap_index = rfind_first_greater_than(nums[pivot_index])
        swap(pivot_index, swap_index)
        reverse_in_range(pivot_index + 1)

