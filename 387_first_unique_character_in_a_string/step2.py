from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # {character: [frequency, first_index]}
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = [0, i]
            count[s[i]][0] += 1

        for c, (freq, first_index) in count.items():
            if freq == 1:
                return first_index
        return -1

class Solution2:
    def firstUniqChar(self, s: str) -> int:
        char_to_first_index = {}
        duplicated_chars = set()
        for i in range(len(s)):
            if s[i] in char_to_first_index:
                del char_to_first_index[s[i]]
                duplicated_chars.add(s[i])
                continue
            if s[i] not in duplicated_chars:
                char_to_first_index[s[i]] = i

        # 順序が保証されているので実質最初の要素にアクセスするだけ
        for character in char_to_first_index:
            return char_to_first_index[character]

        return -1

# return 変えただけ
class Solution3:
    def firstUniqChar(self, s: str) -> int:
        char_to_first_index = {}
        duplicated_chars = set()
        for i in range(len(s)):
            if s[i] in char_to_first_index:
                del char_to_first_index[s[i]]
                duplicated_chars.add(s[i])
                continue
            if s[i] not in duplicated_chars:
                char_to_first_index[s[i]] = i

        if char_to_first_index:
            return char_to_first_index[next(iter(char_to_first_index))]
        return -1
