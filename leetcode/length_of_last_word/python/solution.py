class Solution:
    def lengthOfLastWord(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        counter = 0
        index = len(text) - 1

        while text[index] == " ":
            index -= 1

        while index > -1:
            letter = text[index]
            if letter == " ":
                return counter
            else:
                counter += 1
            index -= 1

        return counter


class Solution:
    def lengthOfLastWord(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: build-in function
        """
        return len(text.split()[-1])


print(Solution().lengthOfLastWord("Hello World") == 5)
print(Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4)
print(Solution().lengthOfLastWord("luffy is still joyboy") == 6)
