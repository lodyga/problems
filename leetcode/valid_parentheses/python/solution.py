class Solution:
    def isValid(self, brackets: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        if len(brackets) % 2:
            return False

        stack = []
        BRACKET_MAP = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for bracket in brackets:
            if bracket in BRACKET_MAP:
                if (stack and stack[-1] == BRACKET_MAP[bracket]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return len(stack) == 0


print(Solution().isValid("()") == True)
print(Solution().isValid("({})") == True)
print(Solution().isValid("(]") == False)
print(Solution().isValid("(})") == False)
print(Solution().isValid("([)") == False)
print(Solution().isValid("") == True)
print(Solution().isValid("[") == False)
print(Solution().isValid(")") == False)
print(Solution().isValid(")(") == False)
