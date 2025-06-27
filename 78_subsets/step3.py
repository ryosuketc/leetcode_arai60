class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        for bit in range(1 << len(nums)):
            subset = []
            for i in range(len(nums)):
                if (bit >> i) & 1:
                    subset.append(nums[i])
            subsets.append(subset)
        return subsets
