class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []

        def permute_helper(perm, nums_left):
            if len(perm) == len(nums):
                all_permutations.append(perm)
                return
            for i, num in enumerate(nums_left):
                new_perm = perm + [nums_left[i]]
                # Exclude nums_left[i]
                new_nums_left = nums_left[:i] + nums_left[i + 1:]
                permute_helper(new_perm, new_nums_left)
        
        permute_helper([], nums)
        return all_permutations
