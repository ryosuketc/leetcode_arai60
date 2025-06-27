class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for bit in range(1 << len(nums)):
            subset = []
            for _, num in enumerate(nums):
                if bit & 1:
                    subset.append(num)
                bit >>= 1
            subsets.append(subset)
        return subsets
