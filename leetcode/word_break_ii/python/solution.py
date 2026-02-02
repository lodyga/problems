class Solution:
    def wordBreak(self, text: str, words: list[str]) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: backtracking
        """
        N = len(text)
        sentence = []
        sentences = []

        def backtrack(index):
            if index == N:
                return sentences.append(" ".join(sentence))
            elif index > N:
                return

            for word in words:
                if word == text[index: index + len(word)]:
                    sentence.append(word)
                    backtrack(index + len(word))
                    sentence.pop()

        backtrack(0)
        return sentences


class Solution:
    def wordBreak(self, text: str, words: list[str]) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: backtracking
        """
        N = len(text)
        sentence = []
        sentences = []
        word_set = set(words)

        def backtrack(start):
            if start == N:
                return sentences.append(" ".join(sentence))
            elif start > N:
                return

            for end in range(start + 1, N + 1):
                word = text[start: end]
                
                if word in word_set:
                    sentence.append(word)
                    backtrack(end)
                    sentence.pop()

        backtrack(0)
        return sentences


class Solution:
    def wordBreak(self, text: str, words: list[str]) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: backtracking with memo
        """
        N = len(text)
        # sentence = []
        word_set = set(words)
        # sentences starting at index
        memo = [-1] * N
        memo.append([""])

        def backtrack(start):
            if start > N:
                return
            elif memo[start] != -1:
                return memo[start]

            sentences = []
            for end in range(start + 1, N + 1):
                word = text[start: end]
                
                if word not in word_set:
                    continue
                
                string = backtrack(end)
                
                if not string:
                    continue
                for substr in string:
                    sentence = word
                    if substr:
                        sentence += " " + substr
                    sentences.append(sentence)
            
            memo[start] = sentences
            return sentences
        
        return backtrack(0)


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


print(sorted(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == sorted(["cats and dog", "cat sand dog"]))
print(sorted(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]))
print(sorted(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) == sorted([]))
