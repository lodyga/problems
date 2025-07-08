class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        """
        Time complexity: O(n3)
            O(word_count*avg_word_length**2)
        Auxiliary space complexity: O(n2)
            O(word_count*avg_word_length)
        Tags: dp, bottom-up with tabulation as hash map
        """
        words.sort(key=len, reverse=True)
        # cache
        word_chain = {word: 1 for word in words}
        longest_str_chain_length = 1

        for word in words:
            for index in range(len(word)):
                predecessor = word[:index] + word[index + 1:]
                if predecessor in word_chain:
                    word_chain[predecessor] = max(word_chain[predecessor], word_chain[word] + 1)
                    longest_str_chain_length = max(longest_str_chain_length, word_chain[predecessor])


        return longest_str_chain_length


print(Solution().longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4)
print(Solution().longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5)
print(Solution().longestStrChain(["abcd", "dbqca"]) == 1)