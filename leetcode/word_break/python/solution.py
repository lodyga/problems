class Solution:
    def wordBreak(self, text: str, word_list: list[str]) -> bool:
        """
        Time complexity: O(n3):
            O(n*m*t)
            n: text length
            m: the number of words
            t: max word length
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        # can construct text starting from index with provided words
        cache = [False] * (len(text) + 1)
        cache[-1] = True
        words = set(word_list)

        for index in reversed(range(len(text))):
            for word in words:
                if text[index: index + len(word)] == word:
                    cache[index] = cache[index + len(word)]
                    if cache[index]:  # early exit
                        break

        return cache[0]


class Solution:
    def wordBreak(self, text: str, word_list: list[str]) -> bool:
        """
        Time complexity: O(n3):
            O(n*m*t)
            n: text length
            m: the number of words
            t: max word length
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {len(text): True}

        def dfs(index):
            if index in memo:
                return memo[index]

            for word in word_list:
                if (
                    text[index: index + len(word)] == word and
                    dfs(index + len(word))
                ):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return dfs(0)


class Solution:
    def wordBreak(self, text: str, word_list: list[str]) -> bool:
        """
        Time complexity: O(n2^n)
            O(t*m^n)
            n: text length
            m: the number of words
            t: max word length
        Auxiliary space complexity: O(n)
        Tags: brute force, tle
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
    def __init__(self):
        self.letters = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        
        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]
            
        node.is_word = True
    
    def search(self, word, left, right):
        node = self.root

        for index in range(left, right + 1):
            letter = word[index]
            if letter in node.letters:
                node = node.letters[letter]
            else:
                return False

        return node.is_word


class Solution:
    def wordBreak(self, text: str, word_list: list[str]) -> bool:
        """
        Time complexity: O(n3):
            O(n*t^2)
            n: text length
            m: the number of words
            t: max word length
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up, trie
        """
        # can construct text starting from index with provided words
        cache = [False] * (len(text) + 1)
        cache[-1] = True
        longest_word = max(len(word) for word in word_list)

        trie = Trie()
        for word in word_list:
            trie.insert(word)


        for left in reversed(range(len(text))):
            # check trie for word starting in `text` from `left` up to `longest word` length
            for right in range(left, min(len(text), left + longest_word)):
                if trie.search(text, left, right):
                    cache[left] = cache[right + 1]  # cache[left + (right - left + 1)]
                if cache[left]:  # early exit
                    break

        return cache[0]


print(Solution().wordBreak("leetcode", ["leet", "code"]) == True)
print(Solution().wordBreak("applepenapple", ["apple", "pen"]) == True)
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False)
print(Solution().wordBreak("cars", ["car", "ca", "rs"]) == True)
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]) == False)