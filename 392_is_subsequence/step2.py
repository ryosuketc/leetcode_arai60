class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)


class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        def _is_subsequence_helper(s_index: int, t_index: int) -> bool:
            if s_index == len(s):
                return True
            if t_index == len(t):
                return False
            
            if s[s_index] == t[t_index]:
                return _is_subsequence_helper(s_index + 1, t_index + 1)
            return _is_subsequence_helper(s_index, t_index + 1)

        return is_subsequence_helper(0, 0)


from bisect import bisect_right
from collections import defaultdict


class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        chat_to_indices = defaultdict(list)
        for t_index, t_char in enumerate(t):
            chat_to_indices[t_char].append(t_index)
        
        # t のどの index まで探索したか (t_index まで探索完了)。まだ探索していないので初期値は -1
        t_traversed_index = -1
        for s_char in s:
            s_char_indices = chat_to_indices[s_char]
            index = bisect_right(s_char_indices, t_traversed_index)
            # otherwise
            # index = bisect_left(s_char_indices, t_traversed_index + 1)
            if index == len(s_char_indices):
                return False
            t_traversed_index = s_char_indices[index]
        return True


class Solution4:
    def isSubsequence(self, s: str, t: str) -> bool:
        # ".*" is needed in the begining too.
        raw_pattern = ".*" + ".*".join(c for c in s)
        pattern = re.compile(raw_pattern)
        return pattern.match(t) != None
