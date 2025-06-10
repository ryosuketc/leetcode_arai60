# WA
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            # 崖を降りている
            if nums[middle] <= nums[-1]:
                if nums[middle] < target:
                    # Search right
                    left = middle + 1
                else:
                    # Search left
                    right = middle - 1
            # 崖を登っている
            else:
                if nums[middle] < target:
                    # Search left
                    right = middle - 1
                else:
                    # Search right
                    left = middle + 1
        return -1

# Accepted
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            # 崖を降りている
            if nums[middle] <= nums[-1]:
                if target < nums[middle]:
                    # Search left
                    right = middle - 1
                elif target <= nums[-1]:
                    # Search right
                    left = middle + 1
                else:
                    # Search left
                    right = middle - 1
            # 崖を登っている
            else:
                if nums[middle] < target:
                    # Search right
                    left = middle + 1
                elif target <= nums[-1]:
                    # Search right
                    left = middle + 1
                else:
                    # Search left
                    right = middle - 1
        return -1
