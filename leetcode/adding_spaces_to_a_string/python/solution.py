class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string, list
            A: two pointers
        """
        words = []
        start = 0

        for end in spaces:
            words.append(s[start: end])
            start = end

        words.append(s[start: len(s)])

        return " ".join(words)


print(Solution().addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15]) == "Leetcode Helps Me Learn")
print(Solution().addSpaces("icodeinpython", [1, 5, 7, 9]) == "i code in py thon")
print(Solution().addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6]) ==" s p a c i n g")
