from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


class SolutionWA:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def permute_helper(nums_left, permutation):
            if not nums_left:
                permutations.append(permutation)
                return
            for i in range(len(nums_left)):
                permutation.append(nums_left[i])
                # Exclude nums_left[i]
                permute_helper(nums_left[:i] + nums_left[i + 1:], permutation)
                permutation.pop()

        permute_helper(nums, [])
        return permutations
