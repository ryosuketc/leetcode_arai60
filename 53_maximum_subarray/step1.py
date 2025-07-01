from math import inf


class SolutionTLE:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -inf
        for i in range(len(nums)):
            subarray = 0
            for j in range(i, len(nums)):
                subarray += nums[j]
                max_subarray = max(max_subarray, subarray)
        return max_subarray
