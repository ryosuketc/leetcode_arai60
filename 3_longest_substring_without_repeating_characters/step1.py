class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0
        characters = set()
        left = 0
        for right in range(len(s)):
            if s[right] in characters:
                while left < right and s[left] != s[right]:
                    characters.remove(s[left])
                    left += 1
                characters.remove(s[left])
                left += 1
            characters.add(s[right])
            longest_substring_length = max(longest_substring_length, right - left + 1)
        return longest_substring_length
