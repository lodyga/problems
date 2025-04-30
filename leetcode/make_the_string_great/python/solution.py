class Solution:
    def makeGood(self, word: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        letter_stack = []

        for letter in word:
            if (letter_stack and
                    letter != letter_stack[-1] and
                    letter.lower() == letter_stack[-1].lower()):
                letter_stack.pop()
            else:
                letter_stack.append(letter)

        return "".join(letter_stack)


print(Solution().makeGood("s") == "s")
print(Solution().makeGood("Mc") == "Mc")
print(Solution().makeGood("Pp") == "")
print(Solution().makeGood("abBAcC") == "")
print(Solution().makeGood("leEeetcode") == "leetcode")
