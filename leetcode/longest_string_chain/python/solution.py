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
        def is_predecessor(index1: int, index2: int) -> bool:
            word1 = words[index1]
            word2 = words[index2]
            if len(word1) + 1 != len(word2):
                return False

            skipped = False
            index1 = 0
            index2 = 0
            while index1 < len(word1):
                if word1[index1] != word2[index2]:
                    if skipped:
                        return False
                    else:
                        skipped = True
                        index1 -= 1
                index1 += 1
                index2 += 1
            return True

        words.sort(key=len)
        cache = [1] * len(words)

        for left in range(len(words) - 1, -1, -1):
            for right in range(left + 1, len(words)):
                if is_predecessor(left, right):
                    cache[left] = max(cache[left], 1 + cache[right])

        return max(cache)


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
        words.sort(key=len, reverse=True)
        cache = {word: 1 for word in words}

        for word in words:
            for index in range(len(word)):
                predecessor = word[: index] + word[index + 1:]
                if predecessor not in cache:
                    continue
                cache[predecessor] = max(cache[predecessor], 1 + cache[word])
        
        return max(cache.values())


print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4)
print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5)
print(Solution().longestStrChain(["abcd", "dbqca"]) == 1)
print(Solution().longestStrChain(["qyssedya", "pabouk", "mjwdrbqwp", "vylodpmwp", "nfyqeowa", "pu", "paboukc", "qssedya", "lopmw", "nfyqowa", "vlodpmw", "mwdrqwp", "opmw", "qsda","neo", "qyssedhyac", "pmw", "lodpmw", "mjwdrqwp", "eo", "nfqwa", "pabuk", "nfyqwa", "qssdya", "qsdya", "qyssedhya", "pabu", "nqwa", "pabqoukc", "pbu", "mw", "vlodpmwp", "x", "xr"]) == 8)
