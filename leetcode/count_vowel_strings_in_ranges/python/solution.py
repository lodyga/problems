class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: prefix sum
        """
        vowels = "aeoiu"
        response = [0] * len(queries)
        bool_words = [word[0] in vowels and word[-1]
                      in vowels for word in words]
        prefix_sum = [0] * (len(words) + 1)

        for index in range(len(words)):
            prefix_sum[index + 1] = prefix_sum[index] + bool_words[index]

        for index, (start, stop) in enumerate(queries):
            response[index] = prefix_sum[stop + 1] - prefix_sum[start]

        return response


print(Solution().vowelStrings(["a", "e", "i"],[[0, 2], [0, 1], [2, 2]]) == [3, 2, 1])
print(Solution().vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]) == [2, 3, 0])