class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_parentheses = []

        def generate_parenthesis_helper(parenthesis, num_open, num_close):
            if len(parenthesis) == 2 * n:
                all_parentheses.append(''.join(parenthesis))
                return
            if num_open < n:
                parenthesis.append('(')
                generate_parenthesis_helper(parenthesis, num_open + 1, num_close)
                parenthesis.pop()
            if num_open > num_close:
                parenthesis.append(')')
                generate_parenthesis_helper(parenthesis, num_open, num_close + 1)
                parenthesis.pop()
        
        generate_parenthesis_helper([], 0, 0)
        return all_parentheses
