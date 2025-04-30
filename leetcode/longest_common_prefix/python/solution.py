class Solution:
    def longestCommonPrefix(self, word_list: list[str]) -> str:
        """
        Time complexity: O(n*k)
            n: number of words
            k: avg word length
        Auxiliary space complexity: O(k)
        """
        prefix = word_list[0]

        for word in word_list[1:]:
            for index, letter in enumerate(word):
                if index < len(prefix) and prefix[index] != letter:
                    prefix = prefix[:index]
                    break
            prefix = prefix[:len(word)]

        return prefix


class TrieNode():
    def __init__(self):
        self.letters = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root

        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]

    def match_prefix(self, word: str):
        node = self.root

        for letter in word:
            if not node.letters:
                return
            elif letter not in node.letters:
                key = list(node.letters.keys())[0]
                node.letters.pop(key)
                return
            key = list(node.letters.keys())[0]
            node = node.letters[key]

        if list(node.letters.keys()):
            key = list(node.letters.keys())[0]
            node.letters.pop(key)

    def get_prefix(self) -> str:
        node = self.root
        word = []

        while list(node.letters.keys()):
            key = list(node.letters.keys())[0]
            word.append(key)
            node = node.letters[key]

        return "".join(word)


class Solution:
    def longestCommonPrefix(self, word_list: list[str]) -> str:
        """
        Time complexity: O(n*k)
            n: number of words
            k: avg word length
        Auxiliary space complexity: O(k)
        Tags: trie
        """
        for word in word_list:
            if not word:
                return ""

        trie = Trie()
        trie.insert(word_list[0])

        for word in word_list[1:]:
            trie.match_prefix(word)

        return trie.get_prefix()


print(Solution().longestCommonPrefix(["flower", "flow"]) == "flow")
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]) == "")