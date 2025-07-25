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
