class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: prefix sum
        """
        vowels = "aeoiu"
        prefix = [0]
    
        for word in words:
            are_vowel_ends = word[0] in vowels and word[-1] in vowels
            prefix.append(prefix[-1] + are_vowel_ends)

        res = []
        
        for start, end in queries:
            res.append(prefix[end + 1] - prefix[start])

        return res


print(Solution().vowelStrings(["a", "e", "i"], [[0, 2], [0, 1], [2, 2]]) == [3, 2, 1])
print(Solution().vowelStrings(["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]) == [2, 3, 0])
