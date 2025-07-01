from math import inf


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        subarray = nums[0]
        for i in range(1, len(nums)):
            subarray = max(nums[i], subarray + nums[i])
            max_sum = max(max_sum, subarray)
        return max_sum


from math import inf


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -inf
        subarray_sum = 0
        for i in range(len(nums)):
            subarray_sum = max(nums[i], subarray_sum + nums[i])
            max_sum = max(max_sum, subarray_sum)
        return max_sum

