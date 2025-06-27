class SolutionStack:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        stack = [([], 0)]
        while stack:
            subset, index = stack.pop()
            if index == len(nums):
                subsets.append(subset)
                continue
            stack.append((subset, index + 1))
            stack.append((subset + [nums[index]], index + 1))
        return subsets


class SolutionRecursion:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def subsets_helper(subset, index):
            if index == len(nums):
                subsets.append(subset)
                return
            subsets_helper(subset, index + 1)
            subsets_helper(subset + [nums[index]], index + 1)

        subsets_helper([], 0)
        return subsets
