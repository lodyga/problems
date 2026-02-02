class Solution:
    def minExtraChar(self, text: str, words: list[str]) -> int:
        """
        Time complexity: O(2^n)
            O(word_count^text_len)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        def dfs(index):
            if index == len(text):
                return 0
            elif index > len(text):
                return len(text) + 1

            res = dfs(index + 1) + 1

            for word in words:
                res = min(res, dfs(index + len(word)))
            return res

        return dfs(0)


class Solution:
    def minExtraChar(self, text: str, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(text length * word count * word lenght)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: top-down
        """
        memo = [-1] * (len(text) + 1)
        memo[len(text)] = 0
        word_set = set(words)
        
        def dfs(index: int) -> int:
            if index > len(text):
                return len(text) + 1
            elif memo[index] != -1:
                return memo[index]

            res = dfs(index + 1) + 1

            for word in word_set:
                if text[index: index + len(word)] == word:
                    res = min(res, dfs(index + len(word)))
            
            memo[index] = res
            return res

        return dfs(0)


class TrieNode:
    def __init__(self) -> None:
        self.letters = {}
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def add(self, word: str) -> None:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                node.letters[letter] = TrieNode()
            node = node.letters[letter]
        node.is_word = True
    
    def has(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                return False
            node = node.letters[letter]
        return node.is_word


class Solution:
    def minExtraChar(self, text: str, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(text length * word lenght**2)
        Auxiliary space complexity: O(n2)
            O(word count * word length) + O(text lenght)
        Tags:
            DS: array, trie
            A: top-down
        """
        longest_word_len = len(max(words, key=len))
        trie = Trie()
        for word in words:
            trie.add(word)

        memo = [-1] * (len(text) + 1)
        memo[len(text)] = 0
        
        def dfs(index: int) -> int:
            if index > len(text):
                return len(text) + 1
            elif memo[index] != -1:
                return memo[index]

            memo[index] = dfs(index + 1) + 1

            for word_len in range(1, longest_word_len + 1):
                if trie.has(text[index: index + word_len]):
                    memo[index] = min(
                        memo[index], 
                        dfs(index + word_len)
                    )
            return memo[index]

        return dfs(0)


class Solution:
    def minExtraChar(self, text: str, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(text length * word count * word lenght)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        cache = [0] * (len(text) + 1)
        word_set = set(words)

        for index in range(len(text) - 1, -1, -1):
            cache[index] = cache[index + 1] + 1

            for word in word_set:
                if (
                    index + len(word) <= len(text) and
                    text[index: index + len(word)] == word
                ):
                    cache[index] = min(
                        cache[index], 
                        cache[index + len(word)]
                    )
                # early exit, if cache is 0 than this is the best case
                if cache[index] == 0:
                    break

        return cache[0]


class Solution:
    def minExtraChar(self, text: str, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(text length * distinct word count * word lenght)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: bottom-up
            check every distinct word length
        """
        cache = [0] * (len(text) + 1)
        word_set = set(words)
        word_lengths = {len(word) for word in word_set}

        for index in range(len(text) - 1, -1, -1):
            cache[index] = cache[index + 1] + 1

            for word_length in word_lengths:
                if (
                    index + word_length <= len(text) and
                    text[index: index + word_length] in word_set
                ):
                    cache[index] = min(
                        cache[index],
                        cache[index + word_length]
                    )
                    # early exit, if cache is 0 than this is the best case
                    if cache[index] == 0:
                        break

        return cache[0]


class Solution:
    def minExtraChar(self, text: str, word_list: list[str]) -> int:
        """
        Time complexity: O(n2)
            O(text length * word lenght)
        Auxiliary space complexity: O(n2)
            O(word count * word length) + O(text lenght)
        Tags:
            DS: trie
            A: bottom-up
        """
        trie = Trie()
        words = set(word_list)
        for word in words:
            trie.add(word)

        cache = [0] * (len(text) + 1)
        longest_word_len = len(max(words, key=len))

        for left in range(len(text) - 1, -1, -1):
            cache[left] = cache[left + 1] + 1
            node = trie.root

            for right in range(left, min(left + longest_word_len, len(text))):
                letter = text[right]

                if letter not in node.letters:
                    break
                node = node.letters[letter]

                if node.is_word:
                    cache[left] = min(cache[left], cache[right + 1])

                    if cache[left] == 0:
                        break

        return cache[0]


print(Solution().minExtraChar("ab", ["a", "b"]) == 0)
print(Solution().minExtraChar("leetcode", ["leet", "code", "leetcode"]) == 0)
print(Solution().minExtraChar("leetscode", ["leet", "code", "leetcode"]) == 1)
print(Solution().minExtraChar("sayhelloworld", ["hello", "world"]) == 3)
print(Solution().minExtraChar("ecolloycollotkvzqpdaumuqgs", ["flbri", "uaaz", "numy", "laper", "ioqyt", "tkvz", "ndjb", "gmg", "gdpbo", "x", "collo", "vuh", "qhozp", "iwk", "paqgn", "m", "mhx", "jgren", "qqshd", "qr", "qpdau", "oeeuq", "c", "qkot", "uxqvx", "lhgid", "vchsk", "drqx", "keaua", "yaru", "mla", "shz", "lby", "vdxlv", "xyai", "lxtgl", "inz", "brhi", "iukt", "f", "lbjou", "vb", "sz", "ilkra", "izwk", "muqgs", "gom", "je"]) == 2)
