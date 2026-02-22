class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(n2 * m)
            n: word count
            m: word length
        Auxiliary space complexity: O(n)
        Tags:
            A: iteration
        """
        counter = 0

        for right in range(len(words)):
            word = words[right]

            for left in range(right):
                fix = words[left]
                fix_len = len(fix)

                if fix == word[: fix_len] == word[len(word) - fix_len:]:
                    counter += 1

        return counter


class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(n2 * m)
            n: word count
            m: word length
        Auxiliary space complexity: O(1)
        Tags:
            A: build-in function
        """
        def isPrefixAndSuffix(fix, word):
            return word.startswith(fix) and word.endswith(fix)

        counter = 0
        for right in range(len(words)):
            for left in range(right):
                if isPrefixAndSuffix(words[left], words[right]):
                    counter += 1

        return counter


print(Solution().countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]) == 4)
print(Solution().countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]) == 2)
print(Solution().countPrefixSuffixPairs(["abab", "ab"]) == 0)
