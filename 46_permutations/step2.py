# Leetcode
class Solution:
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

# NeetCode?
class Solution:
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


# WIP
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutaitons = []
        perms_in_construction = [[]]
        while perms_in_construction:
            perm = perms_in_construction.pop()
            if len(perm) == len(nums):
                permutations.append(perm)
                continue
            for num in nums:
                if num in perm:
                    continue
                perm.append(num)
                perms_in_construction.append(perm)
                perm.pop()
        return permutations
