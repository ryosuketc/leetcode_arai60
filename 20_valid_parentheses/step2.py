# step2-1
class Solution:
    def isValid(self, s: str) -> bool:
        # Closing -> Opening brackets map.
        closing_to_opening_brackets = {")": "(", "}": "{", "]": "["}
        unmatched_open_brackets = []
        for bracket in s:
            if bracket in closing_to_opening_brackets:
                if not unmatched_open_brackets:
                    return False
                actual_bracket = unmatched_open_brackets.pop()
                expected_bracket = closing_to_opening_brackets[bracket]
                if actual_bracket != expected_bracket:
                    return False
            else:
                unmatched_open_brackets.append(bracket)
        
        return not unmatched_open_brackets

# step2-2
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
