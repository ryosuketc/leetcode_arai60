# TLE (in Python , Accepted in Java)
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        cum_sum = [0]
        for i in range(1, len(nums) + 1):
            cum_sum.append(cum_sum[i - 1] + nums[i - 1])

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if cum_sum[j] - cum_sum[i] == k:
                    result += 1
        return result

# TLE (in Python , Accepted in Java)
class Solution3:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            sum_starting_from_i = 0
            for j in range(i, len(nums)):
                sum_starting_from_i += nums[j]
                if sum_starting_from_i == k:
                    result += 1
        return result



# Accepted (O(N))
from collections import defaultdict


class Solution4:
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
