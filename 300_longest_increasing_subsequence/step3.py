class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_lis_lengths = [1] * len(nums)

        def get_max_length_before(index):
            j = 0
            max_length = 0
            for j in range(index):
                if nums[j] < nums[index]:
                    max_length = max(max_length, max_lis_lengths[j])
            return max_length

        for i in range(1, len(nums)):
            max_lis_lengths[i] = max(max_lis_lengths[i], get_max_length_before(i) + 1)
            # max_lis_lengths[i] = get_max_length_before(i) + 1
            # でも十分
        return max(max_lis_lengths)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_lengths = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    max_lengths[i] = max(max_lengths[i], max_lengths[j] + 1)
        return max(max_lengths)
