class Solution:
    def removeStars(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: stack
            A: iteration
        """
        letter_stack = []
        for char in text:
            if letter_stack and char == "*":
                letter_stack.pop()
            else:
                letter_stack.append(char)
        return "".join(letter_stack)


print(Solution().removeStars("leet**cod*e") == "lecoe")
print(Solution().removeStars("erase*****") == "")
