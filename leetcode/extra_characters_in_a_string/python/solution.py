class Solution:
    def minExtraChar(self, text: str, words: list[str]) -> int:
        """
        Time complexity: O(2^n)
            O(word_count^text_length)
        Auxiliary space complexity: O(n)
        Tags:
            A: brute-force
        """
        TEXT_LENGTH = len(text)

        def dfs(idx: int) -> int:
            if idx == TEXT_LENGTH:
                return 0

            # skip
            res = 1 + dfs(idx + 1)

            for word in words:
                word_length = len(word)

                if word == text[idx: idx + word_length]:
                    # take
                    res = min(res, dfs(idx + word_length))

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
        TEXT_LENGTH = len(text)
        memo = [-1] * (TEXT_LENGTH + 1)
        memo[-1] = 0

        def dfs(idx: int) -> int:
            if memo[idx] != -1:
                return memo[idx]

            # skip
            res = 1 + dfs(idx + 1)

            for word in words:
                word_length = len(word)

                if word == text[idx: idx + word_length]:
                    # take
                    res = min(res, dfs(idx + word_length))

            memo[idx] = res
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
            A: bottom-up
        """
        TEXT_LENGTH = len(text)
        cache = [0] * (TEXT_LENGTH + 1)

        for idx in range(TEXT_LENGTH - 1, -1, -1):
            # skip
            cache[idx] = 1 + cache[idx + 1]

            for word in words:
                word_length = len(word)

                if word == text[idx: idx + word_length]:
                    # take
                    cache[idx] = min(
                        cache[idx],
                        cache[idx + word_length]
                    )
                
                # Early exit; if cache[idx] is 0 than this is the lowest number.
                if cache[idx] == 0:
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

        for idx in range(len(text) - 1, -1, -1):
            cache[idx] = cache[idx + 1] + 1

            for word_length in word_lengths:
                if (
                    idx + word_length <= len(text) and
                    text[idx: idx + word_length] in word_set
                ):
                    cache[idx] = min(
                        cache[idx],
                        cache[idx + word_length]
                    )
                    
                    # Early exit; if cache[idx] is 0 than this is the lowest number.
                    if cache[idx] == 0:
                        break

        return cache[0]


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
        LONGEST_WORD_LENGTH = len(max(words, key=len))
        TEXT_LENGTH = len(text)

        trie = Trie()

        for word in words:
            trie.add(word)

        memo = [-1] * (TEXT_LENGTH + 1)
        memo[-1] = 0
        
        def dfs(idx: int) -> int:
            if idx > TEXT_LENGTH:
                return TEXT_LENGTH + 1
            elif memo[idx] != -1:
                return memo[idx]

            memo[idx] = dfs(idx + 1) + 1

            for word_len in range(1, LONGEST_WORD_LENGTH + 1):
                if trie.has(text[idx: idx + word_len]):
                    memo[idx] = min(
                        memo[idx], 
                        dfs(idx + word_len)
                    )
            return memo[idx]

        return dfs(0)



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
        TEXT_LENGTH = len(text)
        words = set(word_list)
        LONGEST_WORD_LENGTH = len(max(words, key=len))
        trie = Trie()
        
        for word in words:
            trie.add(word)

        cache = [0] * (TEXT_LENGTH + 1)

        for left in range(TEXT_LENGTH - 1, -1, -1):
            cache[left] = cache[left + 1] + 1
            node = trie.root

            for right in range(left, min(left + LONGEST_WORD_LENGTH, TEXT_LENGTH)):
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
print(Solution().minExtraChar("ecolloycollotkvzqpdaumuqgs", ["flbri", "uaaz", "numy", "laper", "ioqyt", "tkvz", "ndjb", "gmg", "gdpbo", "x", "collo", "vuh", "qhozp", "iwk", "paqgn", "m", "mhx", "jgren", "qqshd", "qr","qpdau", "oeeuq", "c", "qkot", "uxqvx", "lhgid", "vchsk", "drqx", "keaua", "yaru", "mla", "shz", "lby", "vdxlv", "xyai", "lxtgl", "inz", "brhi", "iukt", "f", "lbjou", "vb", "sz", "ilkra", "izwk", "muqgs", "gom", "je"]) == 2)
