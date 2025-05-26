from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i in range(len(s)):
            if s[i] in count and count[s[i]] == 1:
                return i
        return -1
