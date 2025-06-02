from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_key(word, index):
            return '*'.join([word[:index], word[index + 1:]])

        def get_wildcard_words_to_words_map():
            wildcard_words_to_words = defaultdict(list)
            length = len(wordList[0])
            for word in wordList:
                for i in range(length):
                    key = get_key(word, i)
                    wildcard_words_to_words[key].append(word)
            return wildcard_words_to_words
        
        length = len(beginWord)
        # word, distance
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        wildcard_words_to_words = get_wildcard_words_to_words_map()

        while queue:
            current_word, distance = queue.popleft()
            for i in range(length):
                key = get_key(current_word, i)
                for next_word in wildcard_words_to_words[key]:
                    if next_word == endWord:
                        return distance + 1
                    if next_word in visited:
                        continue
                    visited.add(next_word)
                    queue.append((next_word, distance + 1))

        return 0

