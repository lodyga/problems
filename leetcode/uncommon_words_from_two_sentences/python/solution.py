class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, array
            A: iteration
        """
        word_freq = {}

        for word in s1.split(" ") + s2.split(" "):
            word_freq[word] = word_freq.get(word, 0) + 1

        return [word for word, freq in word_freq.items() if freq == 1]


print(Solution().uncommonFromSentences("this apple is sweet",  "this apple is sour") == ["sweet", "sour"])
print(Solution().uncommonFromSentences("apple apple",  "banana") == ["banana"])
