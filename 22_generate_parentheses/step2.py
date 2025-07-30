class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_parentheses = []

        def backtrack(parentheses, opening, closing):
            if len(parentheses) == 2 * n:
                all_parentheses.append(''.join(parentheses))
                return
            if opening < n:
                parentheses.append('(')
                backtrack(parentheses, opening + 1, closing)
                parentheses.pop()
            if  opening > closing:
                parentheses.append(')')
                backtrack(parentheses, opening, closing + 1)
                parentheses.pop()
        
        backtrack([], 0, 0)
        return all_parentheses
