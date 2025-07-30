class SolutionWA1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        def combination_sum_helper(total, combination, index):
            if total == target:
                combinations.append(combination)
                return
            if total > target:
                return
            if index >= len(candidates):
                return
            candidate = candidates[index]
            # 1. Use the current number and stays in the same number
            combination_sum_helper(total + candidate, combination + [candidate], index)
            # 2. Use the current number and move to the next number
            combination_sum_helper(total + candidate, combination + [candidate], index + 1)
            # 3. Skip the current number
            combination_sum_helper(total, combination, index + 1)
        
        combination_sum_helper(0, [], 0)
        return combinations


class SolutionWA2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        def combination_sum_helper(total, combination, index):
            if index >= len(candidates):
                return
            if total > target:
                return
            if total == target:
                combinations.append(combination)
                return
            candidate = candidates[index]
            # 1. Use the current number and stays in the same number
            combination_sum_helper(total + candidate, combination + [candidate], index)
            # 2. Use the current number and move to the next number
            combination_sum_helper(total + candidate, combination + [candidate], index + 1)
            # 3. Skip the current number
            combination_sum_helper(total, combination, index + 1)
        
        combination_sum_helper(0, [], 0)
        return combinations


class SolutionAC:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        def combination_sum_helper(total, combination, index):
            if index >= len(candidates):
                return
            if total > target:
                return
            if total == target:
                combinations.append(combination)
                return
            candidate = candidates[index]
            # 1. Use the current number and stays in the same number
            combination_sum_helper(total + candidate, combination + [candidate], index)
            # 2. Use the current number and move to the next number
            # combination_sum_helper(total + candidate, combination + [candidate], index + 1)
            # 3. Skip the current number
            combination_sum_helper(total, combination, index + 1)
        
        combination_sum_helper(0, [], 0)
        return combinations

