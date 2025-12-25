class Solution:
    def makeGood(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        letter_stack = []
        for letter in text:
            if (
                letter_stack and
                letter_stack[-1] != letter and
                letter_stack[-1].lower() == letter.lower()
            ):
                letter_stack.pop()
            else:
                letter_stack.append(letter)

        return "".join(letter_stack)


print(Solution().makeGood("s") == "s")
print(Solution().makeGood("Mc") == "Mc")
print(Solution().makeGood("Pp") == "")
print(Solution().makeGood("abBAcC") == "")
print(Solution().makeGood("leEeetcode") == "leetcode")
