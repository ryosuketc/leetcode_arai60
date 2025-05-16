class Solution:
    def isValid(self, s: str) -> bool:
        # Closing -> Opening brackets map.
        brackets_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if stack and char in brackets_map:
                if stack.pop() != brackets_map[char]:
                    return False
            else:
                stack.append(char)
        return not stack