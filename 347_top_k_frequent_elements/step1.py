from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = Counter(nums)
        sorted_frequency_count = sorted(frequency_count.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_frequency_count[:k]]


from collections import Counter


class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = Counter(nums)
        # Swap dict of (num: frequency) to list of (frequency, num) tuples to
        # sort by frequency later.
        frequency_count_list = [(frequency, num) for num, frequency in frequency_count.items()]
        frequency_count_list.sort(reverse=True)
        return [num for frequency, num in frequency_count_list[:k]]
