class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if nums[middle] <= nums[-1]:
                right = middle
            else:
                left = middle + 1
        return nums[left]

# right = len(nums) で初期化しても動く
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] <= nums[-1]:
                right = middle
            else:
                left = middle + 1
        return nums[left] # == right
