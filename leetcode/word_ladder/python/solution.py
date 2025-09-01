from collections import deque


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
        """
        word_set = set(word_list)
        if end_word not in word_set:
            return 0

        word_len = len(begin_word)
        queue = deque([(begin_word, begin_word)])
        self.counter = 0

        def single_diff(word1, word2):
            diff = sum(ord(word1[index]) != ord(word2[index]) 
                       for index in range(word_len))
            return diff == 1

        def bfs():
            while True:
                for _ in range(len(queue)):
                    current_word, prev_word = queue.pop()  # (hot, hit)
                    self.counter += 1

                    for word in word_set:
                        if word == prev_word or word == current_word:
                            continue
                        
                        if single_diff(current_word, word):
                            queue.append((word, current_word))  # (dot, hot), (lot, hot)
                            if word == end_word:
                                return self.counter + 1

        return bfs()


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(Solution().ladderLength("hot", "dot", ["hot", "dot" "dog"]), 3)
# print(Solution().ladderLength("hot", "dog", ["hot", "dog"]), 2)