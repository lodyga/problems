class Solution:
    def removeStars(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        stack = []

        for letter in text:
            if stack and letter == "*":
                stack.pop()
            else:
                stack.append(letter)

        return "".join(stack)
    

print(Solution().removeStars("leet**cod*e") == "lecoe")
print(Solution().removeStars("erase*****") == "")
