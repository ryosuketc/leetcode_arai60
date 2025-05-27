from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix_sum = 0
        prefix_sum_to_count = defaultdict(int)
        prefix_sum_to_count[0] = 1

        for num in nums:
            prefix_sum += num
            target = prefix_sum - k
            result += prefix_sum_to_count[target]
            prefix_sum_to_count[prefix_sum] += 1
            
        return result
