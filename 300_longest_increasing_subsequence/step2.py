class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Longest subsequence length ending at the index.
        longest_subsequence_lengths = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_subsequence_lengths[i] = max(
                        longest_subsequence_lengths[i], longest_subsequence_lengths[j] + 1)
        return max(longest_subsequence_lengths)

class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        for i in range(len(nums)):
            num = nums[i]
            if subsequence[-1] < num:
                subsequence.append(num)
                continue
            j = 0
            while num > subsequence[j]:
                j += 1
            subsequence[j] = num
        return len(subsequence)


from bisect import bisect_left


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        for i in range(len(nums)):
            num = nums[i]
            if subsequence[-1] < num:
                subsequence.append(num)
                continue
            j = bisect_left(subsequence, num)
            subsequence[j] = num

        return len(subsequence)


# Binary search (right を探索の境界として含むパターン)
class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        for i in range(len(nums)):
            num = nums[i]
            if subsequence[-1] < num:
                subsequence.append(num)
                continue
            left = 0
            right = len(subsequence) - 1
            while left <= right:
                mid = (left + right) // 2
                if subsequence[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            subsequence[left] = num

        return len(subsequence)


# Binary search (right を探索の境界として含まないパターン)
class Solution4:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        for i in range(len(nums)):
            num = nums[i]
            if subsequence[-1] < num:
                subsequence.append(num)
                continue
            left = 0
            right = len(subsequence)
            while left < right:
                mid = (left + right) // 2
                if subsequence[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            subsequence[left] = num
        return len(subsequence)


# Binary search (関数切り出し)
class Solution5:
    def _search_insert_position(self, sequence, num):
            left = 0
            right = len(sequence)
            while left < right:
                mid = (left + right) // 2
                if sequence[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left

    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        for i in range(len(nums)):
            num = nums[i]
            if subsequence[-1] < num:
                subsequence.append(num)
                continue
            insert_index = self._search_insert_position(subsequence, num)
            subsequence[insert_index] = num
        return len(subsequence)
