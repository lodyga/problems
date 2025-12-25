class Solution:
    def longestCommonPrefix(self, words: list[str]) -> str:
        """
        Time complexity: O(n*k)
            n: number of words
            k: avg word length
        Auxiliary space complexity: O(k)
        Tags: 
            DS: list
            A: iteration
        """
        prefix = list(words[0])

        for word in words:
            while len(prefix) > len(word):
                prefix.pop()

            for index in range(len(prefix)):
                if prefix[index] != word[index]:
                    while len(prefix) > index:
                        prefix.pop()
                    break

            if len(prefix) == 0:
                return ""

        return "".join(prefix)


class TrieNode():
    def __init__(self):
        self.letters = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def push(self, word: str) -> None:
        node = self.root

        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]

    def match_prefix(self, word: str) -> bool:
        node = self.root
        if not node.letters:
            return True
        
        for letter in word:
            if letter in node.letters:
                node = node.letters[letter]
            else:
                if node.letters:
                    letter = next(iter(node.letters))
                    node.letters.pop(letter)
                break
        
        if node.letters:
            letter = next(iter(node.letters))
            node.letters.pop(letter)
        
        return False
        

    def get_prefix(self) -> str:
        node = self.root
        prefix = []

        while node:
            if node.letters:
                prefix.append(next(iter(node.letters)))
                node = node.letters[next(iter(node.letters))]
            else:
                node = None

        return "".join(prefix)


class Solution:
    def longestCommonPrefix(self, words: list[str]) -> str:
        """
        Time complexity: O(n*k)
            n: number of words
            k: avg word length
        Auxiliary space complexity: O(k)
        Tags: 
            DS: trie
            A: iteration
        """
        for word in words:
            if not word:
                return ""

        # prefix candidate
        trie = Trie()
        trie.push(words[0])

        for word in words:
            if word == "":
                return ""
            if trie.match_prefix(word):
                return ""

        return trie.get_prefix()


print(Solution().longestCommonPrefix(["flower", "flow"]) == "flow")
print(Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]) == "")
print(Solution().longestCommonPrefix(["aaa", "aa", "aaa"]) == "aa")
