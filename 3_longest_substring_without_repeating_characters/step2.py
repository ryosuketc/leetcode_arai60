class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len


# WA - left のアップデートが間違っている
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen_index = {}
        left = 0
        for right in range(len(s)):
            if s[right] in seen_index:
                left = seen_index[s[right]] + 1
                del seen_index[s[right]]
            seen_index[s[right]] = right
            max_len = max(max_len, right - left + 1)
            print(f'left={left}, right={right}, max_len={max_len}')
        return max_len


# インデックスで管理する
class Solution2_1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen_index = {}
        left = 0
        for right in range(len(s)):
            if s[right] in seen_index:
                left = max(left, seen_index[s[right]] + 1)
            seen_index[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len


# インデックスで管理する (条件分岐削除)
class Solution2_2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen_index = {}
        left = 0
        for right in range(len(s)):
            left = max(left, seen_index.get(s[right], -1) + 1)
            seen_index[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len
