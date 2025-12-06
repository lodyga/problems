from collections import deque


class Solution:
    def wordBreak(self, text: str, words: list[str]) -> bool:
        """
        Time complexity: O(n3):
            O(n*m*t)
            n: text length
            m: word count
            t: avg word length
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: top-down
        """
        def is_word_in_segment(left, word):
            """
            Equivalent of:
            text[left: left + len(word)] == word
            """
            if left + len(word) > len(text):
                return False
            for index in range(len(word)):
                if text[left + index] != word[index]:
                    return False
            return True

        word_set = set(words)
        memo = [None] * (len(text) + 1)
        memo[-1] = True

        def dfs(index):
            if memo[index] is not None:
                return memo[index]

            is_segmented = False
            for word in word_set:
                if (
                    is_word_in_segment(index, word) and
                    dfs(index + len(word))
                ):
                    is_segmented = True
                    break

            memo[index] = is_segmented
            return is_segmented

        return dfs(0)

    def wordBreak(self, text: str, words: list[str]) -> bool:
        """
        Time complexity: O(n3):
            O(n*m*t)
            n: text length
            m: word count
            t: avg word length
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: bottom-up
        """
        def is_word_in_segment(left, word):
            """
            Equivalent of:
            text[left: left + len(word)] == word
            """
            if left + len(word) > len(text):
                return False
            for index in range(len(word)):
                if text[left + index] != word[index]:
                    return False
            return True

        cache = [False] * (len(text) + 1)
        cache[-1] = True
        word_set = set(words)

        for index in range(len(text) - 1, -1, -1):
            for word in word_set:
                if (
                    is_word_in_segment(index, word) and
                    cache[index + len(word)]
                ):
                    cache[index] = True
                    break

        return cache[0]


class Solution2:
    def wordBreak(self, text: str, word_list: list[str]) -> bool:
        """
        Time complexity: O(n2^n)
            O(t*m^n)
            n: text length
            m: word count
            t: avg word length
        Auxiliary space complexity: O(n)
        Tags: brute-force
        """
        def dfs(index):
            if index == len(text):
                return True

            for word in word_list:
                if (
                    text[index: index + len(word)] == word and
                    dfs(index + len(word))
                ):
                    return True

            return False

        return dfs(0)


class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word) -> None:
        node = self.root

        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]
        node.is_word = True

    def lookup(self, left, right, text) -> bool:
        node = self.root

        for index in range(left, right + 1):
            letter = text[index]
            if letter not  in node.letters:
                return False
            node = node.letters[letter]
        return node.is_word


class Solution:
    def wordBreak(self, text: str, words: list[str]) -> bool:
        """
        Time complexity: O(n3):
            O(n*t^2 + m)
            n: text length
            m: word count
            t: longest word length
        Auxiliary space complexity: O(n+m*t)
        Tags: 
            DS: tire, array
            A: bottom-up
        """
        trie = Trie()
        for word in words:
            trie.add(word)

        cache = [False] * (len(text) + 1)
        cache[-1] = True
        max_word_length = len(max(words, key=len))
        min_word_length = len(min(words, key=len))

        for left in range(len(text) - min_word_length, -1, -1):
            for right in range(left, min(left + max_word_length, len(text))):
                if (
                    trie.lookup(left, right, text) and
                    cache[right + 1]
                ):
                    cache[left] = True
                    break

        return cache[0]


class Solution:
    def wordBreak(self, text: str, words: list[str]) -> bool:
        """
        Time complexity: O(n3):
            O(n*m*t)
            n: text length
            m: word count
            t: avg word length
        Auxiliary space complexity: O(n+m*t)
        Tags: 
            DS: queue
            A: bottom-up
        """
        def is_word_in_segment(left, word):
            """
            Equivalent of:
            text[left: left + len(word)] == word
            """
            if left + len(word) > len(text):
                return False
            for index in range(len(word)):
                if text[left + index] != word[index]:
                    return False
            return True

        word_set = set(words)

        def bfs(index):
            queue = deque([index])
            visited = [False] * (len(text) + 1)
            visited[0] = True

            while queue:
                index = queue.popleft()
                if index == len(text):
                    return True

                for word in word_set:
                    if (
                        index + len(word) <= len(text) and
                        visited[index + len(word)] is False and
                        is_word_in_segment(index, word)
                    ):
                        queue.append(index + len(word))
                        visited[index + len(word)] = True

            return False

        return bfs(0)


print(Solution().wordBreak("leetcode", ["leet", "code"]) == True)
print(Solution().wordBreak("applepenapple", ["apple", "pen"]) == True)
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False)
print(Solution().wordBreak("cars", ["car", "ca", "rs"]) == True)
print(Solution().wordBreak("aaaaaaa", ["aaaa", "aa"]) == False)
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]) == False)
