# bisect - accepted
class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        def priority(num):
            return (num <= nums[-1], target <= num)
        target_index = bisect_left(nums, priority(target), key=priority)
        if nums[target_index] != target:
            return -1
        return target_index

# Accepted
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            # past cliff
            if nums[middle] <= nums[-1]:
                # right of middle is sorted
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            # before cliff
            else:
                # left of middle is sorted
                if nums[left]<= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1


# 半開で書こうとしたが失敗
class Solution3_WA:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] <= nums[-1]:
                if nums[middle] < target < nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1

class Solution3_AC:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] <= nums[-1]:
                # middle を含む右側は昇順
                if nums[middle] < target <= nums[right - 1]:
                    left = middle + 1
                else:
                    right = middle
            else:
                # middle を含む左側は昇順
                if nums[left] <= target < nums[middle]:
                    right = middle
                else:
                    left = middle + 1
        return -1
