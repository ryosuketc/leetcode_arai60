from collections import defaultdict
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def make_graph():
            graph = defaultdict(list)
            length = len(wordList[0])
            for word in wordList:
                for i in range(length):
                    key = '*'.join([word[:i], word[i + 1:]])
                    graph[key].append(word)
            return graph
        
        length = len(beginWord)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        graph = make_graph()

        while queue:
            current_word, distance = queue.popleft()
            for i in range(length):
                key = '*'.join([current_word[:i], current_word[i + 1:]])
                for next_word in graph[key]:
                    if next_word == endWord:
                        return distance + 1
                    if next_word in visited:
                        continue
                    visited.add(next_word)
                    queue.append((next_word, distance + 1))
            # LeetCode の解答にはあるけどなくても動く。特に必要ない？
            # graph[key] = []

        return 0
