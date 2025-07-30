class SolutionRecursion:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def combination_sum_helper(index, total, combination):
            if index >= len(candidates):
                return
            if total > target:
                return
            if total == target:
                combinations.append(combination)
                return
            candidate = candidates[index]
            combination_sum_helper(index, total + candidate, combination + [candidate])
            combination_sum_helper(index + 1, total, combination)
        
        combination_sum_helper(0, 0, [])
        return combinations


class SolutionStack:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        stack = [(0, 0, [])]
        while stack:
            index, total, combination = stack.pop()
            if index >= len(candidates):
                continue
            if total > target:
                continue
            if total == target:
                combinations.append(combination)
                continue
            candidate = candidates[index]
            stack.append((index, total + candidate, combination + [candidate]))
            stack.append((index + 1, total, combination))
        
        return combinations
