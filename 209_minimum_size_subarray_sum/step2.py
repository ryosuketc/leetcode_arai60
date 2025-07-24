from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = inf
        running_sum = 0
        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum >= target:
                min_len = min(min_len, right - left + 1)
                running_sum -= nums[left]
                left += 1
        if min_len == inf:
            return 0
        return min_len
