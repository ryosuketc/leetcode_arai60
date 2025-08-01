class SolutionWA:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        s_index = 0
        for t_char in t:
            if s[s_index] == t_char:
                s_index += 1
                if s_index == len(s):
                    return True
        return False



class SolutionAC:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(t) < len(s):
            return False
        s_index = 0
        for t_char in t:
            if s[s_index] == t_char:
                s_index += 1
                if s_index == len(s):
                    return True
        return False
