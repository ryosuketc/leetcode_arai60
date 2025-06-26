class SolutionStack:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        perms_in_construction = [[]]
        while perms_in_construction:
            perm = perms_in_construction.pop()
            if len(perm) == len(nums):
                permutations.append(perm[:])
                continue
            for num in nums:
                if num in perm:
                    continue
                new_perm = perm + [num]
                perms_in_construction.append(new_perm)
        return permutations


class SolutionRecursion:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def permute_helper(perm):
            # perm: Permutation under constrution
            if len(perm) == len(nums):
                permutations.append(perm[:])
                return
            for num in nums:
                if num in perm:
                    continue
                new_perm = perm + [num]
                permute_helper(new_perm)
                # 上の 2 行はこうも書ける
                # perm.append(num)
                # permute_helper(perm)
                # perm.pop()

        permute_helper([])
        return permutations



# Leetcode
class SolutionLeetCode:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans

# https://discord.com/channels/1084280443945353267/1233603535862628432/1238878881910493255
class SolutionNumsLeft:
    def permute(self, nums: List[int]) -> List[List[int]]:
        all_permutations = []
        # (WIP permutation, nums_left)
        stack = [([], nums)]
        while stack:
            permutation_so_far, nums_left = stack.pop()
            if len(permutation_so_far) == len(nums):
                all_permutations.append(permutation_so_far)
                continue
            for i, num in enumerate(nums_left):
                new_permutation = permutation_so_far + [num]
                new_nums_left = nums_left[:i] + nums_left[i+1:]
                stack.append((new_permutation, new_nums_left))
        return all_permutations


class SolutionStep1Fixed:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def permute_helper(nums_left, permutation):
            if not nums_left:
                permutations.append(permutation[:])
                return
            for i in range(len(nums_left)):
                permutation.append(nums_left[i])
                # Exclude nums_left[i]
                permute_helper(nums_left[:i] + nums_left[i + 1:], permutation[:])
                permutation.pop()

        permute_helper(nums, [])
        return permutations



# NeetCode
class SolutionNeetCode:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(k):
            if k == n:
                output.append(nums[:])
            for i in range(k, n):
                nums[k], nums[i] = nums[i], nums[k]
                backtrack(k + 1)
                nums[k], nums[i] = nums[i], nums[k]
        n = len(nums)
        output = []
        backtrack(0)
        return output
