from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_key(word, index):
            return f'{word[:index]}*{word[index + 1:]}'

        def get_words_map():
            words_map = defaultdict(list)
            for word in wordList:
                for i in range(len(word)):
                    key = get_key(word, i)
                    words_map[key].append(word)
            return words_map

        length = len(beginWord)
        words_map = get_words_map()
        visited = {beginWord}
        queue = deque([(beginWord, 1)])

        while queue:
            current_word, distance = queue.popleft()
            for i in range(length):
                key = get_key(current_word, i)
                for next_word in words_map[key]:
                    if next_word == endWord:
                        return distance + 1
                    if next_word in visited:
                        continue
                    visited.add(next_word)
                    queue.append((next_word, distance + 1))
        
        return 0
