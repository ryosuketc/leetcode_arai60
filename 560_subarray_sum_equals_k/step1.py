# TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            sum_starting_from_i = nums[i]
            # subarray of one element (nums[i])
            if sum_starting_from_i == k:
                result += 1
            for j in range(i + 1, len(nums)):
                sum_starting_from_i += nums[j]
                if sum_starting_from_i == k:
                    result += 1
        return result
