from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        count_to_num = [(count, num) for num, count in nums_count.items()]
        count_to_num.sort(reverse=True)
        return [num for _, num in count_to_num[:k]]
