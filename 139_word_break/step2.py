# Recursion
from functools import cache


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


# Bottom-up DP (前から)
class SolutionDpFromFront:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        segmented = [False] * (len(s) + 1)
        segmented[0] = True
        words = set(wordDict)
        for i in range(1, len(s) + 1):
            for word in words:
                word_start_index = i - len(word)
                if word_start_index < 0:
                    continue
                if not s.startswith(word, word_start_index):
                    continue
                if segmented[word_start_index]:
                    segmented[i] = True
        return segmented[-1]


# Bottom-up DP (後ろから)
class SolutionDpFromBack:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        segmented = [False] * (len(s) + 1)
        segmented[len(s)] = True
        words = set(wordDict)
        for i in reversed(range(len(s))):
            for word in words:
                word_end_index = i + len(word)
                if word_end_index > len(s):
                    continue
                if not s.startswith(word, i):
                    continue
                if segmented[word_end_index]:
                    segmented[i] = True
        return segmented[0]



# only ref: https://neetcode.io/problems/implement-prefix-tree
# 数年前にははこんなのを書いていたみたい。
class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['*'] = ''


    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '*' in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True
        