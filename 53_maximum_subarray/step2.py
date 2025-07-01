class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray = nums[0]
        max_subarray = nums[0]
        for i in range(1, len(nums)):
            subarray = max(nums[i], subarray + nums[i])
            max_subarray = max(max_subarray, subarray)
        return max_subarray


class Solution2WA:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sums = nums[:]
        for i in range(1, len(nums)):
            # max_sums[i] == nums[i] by default.
            max_sums[i] = max(max_sums[i], max_sums[i - 1] + nums[i])
        print(max_sums)
        return max_sums[-1]


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sums = nums[:]
        for i in range(1, len(nums)):
            # max_sums[i] == nums[i] by default.
            max_sums[i] = max(max_sums[i], max_sums[i - 1] + nums[i])
        return max(max_sums)



from math import inf


class Solution3TLE:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_subarray_helper(left, right):
            if left > right:
                return -inf
            mid = (left + right) // 2
            max_sum_left = 0
            running_sum = 0
            # Get max_sum (continuous elemennts starting from but excluding middle)
            for i in reversed(range(0, mid)):
                running_sum += nums[i]
                max_sum_left = max(max_sum_left, running_sum)
            max_sum_right = 0
            running_sum = 0
            for i in range(mid + 1, len(nums)):
                running_sum += nums[i]
                max_sum_right = max(max_sum_right, running_sum)
            max_sum_with_mid = max_sum_left + nums[mid] + max_sum_right

            max_sum_only_left = max_subarray_helper(left, mid - 1)
            max_sum_only_right = max_subarray_helper(mid + 1, right)

            return max(max_sum_with_mid, max_sum_only_left, max_sum_only_right)
        
        return max_subarray_helper(0, len(nums) - 1)




from math import inf


class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_subarray_helper(left, right):
            if left > right:
                return -inf
            mid = (left + right) // 2
            max_sum_left = 0
            running_sum = 0
            # Get max_sum (continuous elemennts starting from but excluding middle)
            for i in reversed(range(left, mid)):
                running_sum += nums[i]
                max_sum_left = max(max_sum_left, running_sum)
            max_sum_right = 0
            running_sum = 0
            for i in range(mid + 1, right + 1):
                running_sum += nums[i]
                max_sum_right = max(max_sum_right, running_sum)
            max_sum_with_mid = max_sum_left + nums[mid] + max_sum_right

            max_sum_only_left = max_subarray_helper(left, mid - 1)
            max_sum_only_right = max_subarray_helper(mid + 1, right)

            return max(max_sum_with_mid, max_sum_only_left, max_sum_only_right)
        
        return max_subarray_helper(0, len(nums) - 1)



from math import inf


class Solution4:
    def maxSubArray(self, nums: List[int]) -> int:
        def max_subarray_helper(left, right):
            if left >= right:
                return -inf
            mid = (left + right) // 2
            max_sum_left = 0
            running_sum = 0
            # Get max_sum (continuous elemennts starting from but excluding middle)
            for i in reversed(range(left, mid)):
                running_sum += nums[i]
                max_sum_left = max(max_sum_left, running_sum)
            max_sum_right = 0
            running_sum = 0
            for i in range(mid + 1, right):
                running_sum += nums[i]
                max_sum_right = max(max_sum_right, running_sum)
            max_sum_with_mid = max_sum_left + nums[mid] + max_sum_right

            max_sum_only_left = max_subarray_helper(left, mid)
            max_sum_only_right = max_subarray_helper(mid + 1, right)

            return max(max_sum_with_mid, max_sum_only_left, max_sum_only_right)
        
        return max_subarray_helper(0, len(nums))
