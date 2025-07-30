class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        seen_index = {}
        for right in range(len(s)):
            if s[right] in seen_index:
                left = max(left, seen_index[s[right]] + 1)
            max_len = max(max_len, right - left + 1)
            seen_index[s[right]] = right
        return max_len
