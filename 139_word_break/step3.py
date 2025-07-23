class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        @cache
        def can_split(index):
            if index == len(s):
                return True
            for word in word_set:
                if not s.startswith(word, index):
                    continue
                if can_split(index + len(word)):
                    return True
            return False
        
        return can_split(0)
