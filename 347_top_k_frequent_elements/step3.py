import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = collections.Counter(nums)
        count_to_nums = [(count, num) for num, count in nums_count.items()]
        count_to_nums.sort(reverse=True)
        return [num for _, num in count_to_nums[:k]]
