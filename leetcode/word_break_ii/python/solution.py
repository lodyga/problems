class Solution:
    def wordBreak(self, text: str, word_list: list[str]) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        words = set(word_list)
        sentence = []
        sentences = []

        def dfs(index):
            if index == len(text):
                sentences.append(" ".join(sentence))
                return
            
            for word in words:
                if text[index: index + len(word)] == word:
                    sentence.append(word)
                    dfs(index + len(word))
                    sentence.pop()

        dfs(0)
        return sentences


class Solution:
    def wordBreak(self, text: str, word_list: list[str]) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        words = set(word_list)
        sentence = []
        sentences = []

        def dfs(index):
            if index == len(text):
                sentences.append(" ".join(sentence))
                return

            for right in range(index, len(text)):
                word = text[index: right + 1]
                if word in words:
                    sentence.append(word)
                    dfs(index + len(word))
                    sentence.pop()

        dfs(0)
        return sentences


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
    
    def has(self, word) -> bool:
        node = self.root
        for letter in word:
            if letter in node.letters:
                node = node.letters[letter]
            else:
                return False
        return node.is_word


class Solution:
    def wordBreak(self, text: str, word_list: list[str]) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        words = set(word_list)
        sentence = []
        sentences = []
        word_length = 0

        word_trie = Trie()
        for word in words:
            word_trie.add(word)
            word_length = max(word_length, len(word))

        def dfs(index):
            if index == len(text):
                sentences.append(" ".join(sentence))
                return

            for right in range(index, min(len(text), index + word_length)):
                word = text[index: right + 1]
                if word_trie.has(word):
                    sentence.append(word)
                    dfs(index + len(word))
                    sentence.pop()

        dfs(0)
        return sentences


print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"])
print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), [])
print(sorted(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == sorted(["cats and dog", "cat sand dog"]))
print(sorted(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]))
print(sorted(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) == sorted([]))