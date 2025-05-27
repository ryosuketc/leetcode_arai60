class Solution:
    def isValid(self, s: str) -> bool:
        # Closing -> Opening brackets map.
        closing_to_opening_brackets = {")": "(", "}": "{", "]": "["}
        unmatched_open_brackets = []

        for bracket in s:
            is_opening = bracket in closing_to_opening_brackets.values()
            if is_opening:
                unmatched_open_brackets.append(bracket)
                continue
            
            if not unmatched_open_brackets:
                return False
            actual = unmatched_open_brackets.pop()
            expected = closing_to_opening_brackets[bracket]
            if actual != expected:
                return False

        return not unmatched_open_brackets


class Solution2:
    def isValid(self, s: str) -> bool:
        # Closing -> Opening brackets map.
        closing_to_opening_brackets = {")": "(", "}": "{", "]": "["}
        unmatched_opening_brackets = []

        for bracket in s:
            is_opening = bracket in closing_to_opening_brackets.values()
            if is_opening:
                unmatched_opening_brackets.append(bracket)
                continue
            
            if not unmatched_opening_brackets:
                return False
            actual = unmatched_opening_brackets.pop()
            expected = closing_to_opening_brackets[bracket]
            if actual != expected:
                return False
        
        return not unmatched_opening_brackets
