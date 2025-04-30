class Solution:
    def lengthOfLastWord(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        return len(text.split()[-1])


print(Solution().lengthOfLastWord("Hello World") == 5)
print(Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4)
print(Solution().lengthOfLastWord("luffy is still joyboy") == 6)
