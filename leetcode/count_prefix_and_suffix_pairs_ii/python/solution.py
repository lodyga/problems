class TrieNode:
    def __init__(self) -> None:
        self.letters = {}  # {(prefix letter, suffix letter): {}}
        # self.is_word = False
        self.counter = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
        node = self.root

        for pair in zip(word, reversed(word)):
            if pair not in node.letters:
                node.letters[pair] = TrieNode()
            node = node.letters[pair]
            node.counter += 1
        # node.is_word = True

    def count(self, word):
        node = self.root

        for pair in zip(word, reversed(word)):
            if pair not in node.letters:
                return 0
            node = node.letters[pair]

        return node.counter


class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Time complexity: O(n2)
            O(n * m)
            n: word count
            m: word length
        Auxiliary space complexity: O(n * m)
        Tags: trie
        """
        trie = Trie()
        counter = 0
        for word in reversed(words):
            counter += trie.count(word)
            trie.add(word)
        return counter


print(Solution().countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]) == 4)
print(Solution().countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]) == 2)
print(Solution().countPrefixSuffixPairs(["abab", "ab"]) == 0)
