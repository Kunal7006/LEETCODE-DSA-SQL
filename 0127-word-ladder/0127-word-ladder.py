
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord, 1))

        st = set(wordList)
        st.discard(beginWord)

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                original = word[i]

                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in st:
                        st.remove(newWord)
                        q.append((newWord, steps + 1))

        return 0
