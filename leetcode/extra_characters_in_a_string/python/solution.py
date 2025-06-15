class Solution:
    def minExtraChar(self, text: str, word_list: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(text length * word count * word lenght)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up, hash set
        check every word iteself
        """
        cache = [0] * (len(text) + 1)
        words = set(word_list)

        for index in reversed(range(len(text))):
            # set default cache as if word is not found
            cache[index] = cache[index + 1] + 1

            for word in words:
                if (
                    index + len(word) <= len(text) and
                    text[index: index + len(word)] == word
                ):
                    cache[index] = min(cache[index],
                                       cache[index + len(word)])

                    # early exit, if cache is 0 than this is the best case
                    if cache[index] == 0:
                        break

        return cache[0]


class Solution:
    def minExtraChar(self, text: str, word_list: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(text length * distinct word length * word lenght)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up, hash set
        check every word length
        """
        cache = [0] * (len(text) + 1)
        words = set(word_list)
        word_lengths = {len(word) for word in words}

        for index in reversed(range(len(text))):
            # set default cache as if word is not found
            cache[index] = cache[index + 1] + 1

            for word_length in word_lengths:
                if (
                    index + word_length <= len(text) and
                    text[index: index + word_length] in words
                ):
                    cache[index] = min(cache[index],
                                       cache[index + word_length])

                    # early exit, if cache is 0 than this is the best case
                    if cache[index] == 0:
                        break

        return cache[0]


class Solution:
    def minExtraChar(self, text: str, word_list: list[str]) -> int:
        """
        Time complexity: O(2^n)
            O(word_list^text)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index):
            if index == len(text):
                return 0
            elif index > len(text):
                return len(text) + 1

            res = len(text) + 1
            for word in word_list:
                res = min(res, dfs(index + len(word)))
            res = min(res, dfs(index + 1) + 1)
            return res

        return dfs(0)


class Solution:
    def minExtraChar(self, text: str, word_list: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(text length * word count * word lenght)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down, hash set
        """
        cache = {len(text): 0}
        words = set(word_list)

        def dfs(index):
            if index in cache:
                return cache[index]
            elif index > len(text):
                return len(text) + 1

            cache[index] = dfs(index + 1) + 1
            for word in words:
                cache[index] = min(cache[index],
                                   dfs(index + len(word)))
            return cache[index]

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

    def search(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter not in node.letters:
                return False
            node = node.letters[letter]
        return node.is_word


class Solution:
    def minExtraChar(self, text: str, word_list: list[str]) -> int:
        """
        Time complexity: O(n2)
            O(text length * word lenght)
        Auxiliary space complexity: O(n2)
            O(text lenght) + O(word count * word length)
        Tags: dp, bottom-up, trie
        """
        word_trie = Trie()
        words = set(word_list)
        for word in words:
            word_trie.add(word)

        cache = [0] * (len(text) + 1)
        longest_word_length = max(len(word) for word in words)

        for left in reversed(range(len(text))):
            cache[left] = cache[left + 1] + 1
            node = word_trie.root

            for right in range(left, min(left + longest_word_length, len(text))):
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