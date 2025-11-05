class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(n2 * m)
            n: word count
            m: word length
        Auxiliary space complexity: O(1)
        Tags: build-in function
        """
        def isPrefixAndSuffix(word1, word2):
            return word2.startswith(word1) and word2.endswith(word1)

        counter = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    counter += 1
        return counter


print(Solution().countPrefixSuffixPairs(["a", "aba", "ababa", "aa"]) == 4)
print(Solution().countPrefixSuffixPairs(["pa", "papa", "ma", "mama"]) == 2)
print(Solution().countPrefixSuffixPairs(["abab", "ab"]) == 0)
