class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(word count * avg word length**2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, hash set
            A: top-down
        """
        word_set = set(words)
        memo = {"": 0}

        def dfs(word: str) -> int:
            if word in memo:
                return memo[word]
            elif word not in word_set:
                return 0

            res = 0

            for idx in range(len(word)):
                res = max(res, 1 + dfs(word[: idx] + word[idx + 1:]))

            memo[word] = res
            return res

        return max(dfs(word) for word in words)


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(word count * avg word length**2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: bottom-up
        """
        words.sort(key=len)
        cache = {}

        for word in words:
            cache[word] = 1
            
            for idx in range(len(word)):
                predecessor = word[: idx] + word[idx + 1: ]

                if predecessor in cache:
                    cache[word] = max(cache[word], 1 + cache[predecessor])

        return max(cache.values())


class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(word count**2 * avg word length)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        def is_predecessor(idx1: int, idx2: int) -> bool:
            word1 = words[idx1]
            word2 = words[idx2]
            if len(word1) + 1 != len(word2):
                return False

            skipped = False
            idx1 = 0
            idx2 = 0
            
            while idx1 < len(word1):
                if word1[idx1] != word2[idx2]:
                    if skipped:
                        return False
                    else:
                        skipped = True
                        idx1 -= 1
                idx1 += 1
                idx2 += 1
            return True

        words.sort(key=len)
        cache = [1] * len(words)

        for left in range(len(words) - 1, -1, -1):
            for right in range(left + 1, len(words)):
                if is_predecessor(left, right):
                    cache[left] = max(cache[left], 1 + cache[right])

        return max(cache)


print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4)
print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5)
print(Solution().longestStrChain(["abcd", "dbqca"]) == 1)
print(Solution().longestStrChain(["qyssedya", "pabouk", "mjwdrbqwp", "vylodpmwp", "nfyqeowa", "pu", "paboukc", "qssedya", "lopmw", "nfyqowa", "vlodpmw", "mwdrqwp", "opmw", "qsda", "neo", "qyssedhyac", "pmw", "lodpmw", "mjwdrqwp", "eo", "nfqwa", "pabuk", "nfyqwa", "qssdya", "qsdya", "qyssedhya", "pabu", "nqwa", "pabqoukc", "pbu", "mw", "vlodpmwp", "x", "xr"]) == 8)
