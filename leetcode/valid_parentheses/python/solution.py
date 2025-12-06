class Solution:
    def isValid(self, bracket_list: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        if len(bracket_list) % 2:
            return False

        bracket_stack = []
        CLOSING_BRACKET = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for bracket in bracket_list:
            if bracket in CLOSING_BRACKET:
                if bracket_stack and bracket_stack[-1] == CLOSING_BRACKET[bracket]:
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(bracket)

        return len(bracket_stack) == 0


print(Solution().isValid("()") == True)
print(Solution().isValid("({})") == True)
print(Solution().isValid("(]") == False)
print(Solution().isValid("(})") == False)
print(Solution().isValid("([)") == False)
print(Solution().isValid("") == True)
print(Solution().isValid("[") == False)
