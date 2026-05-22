class Solution:
    def lengthOfLastWord(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        res = 0
        idx = len(text) - 1

        while text[idx] == " ":
            idx -= 1

        while idx > -1 and text[idx] != " ":
            res += 1
            idx -= 1

        return res


print(Solution().lengthOfLastWord("Hello World") == 5)
print(Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4)
print(Solution().lengthOfLastWord("luffy is still joyboy") == 6)
print(Solution().lengthOfLastWord("y") == 1)
