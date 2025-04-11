class Solution:
    def isValid(self, bracket_list: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        if len(bracket_list) % 2 != 0:
            return False

        stacked_brackets = []
        closing_bracket = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for bracket in bracket_list:
            if bracket in closing_bracket:
                if (stacked_brackets and
                        stacked_brackets[-1] == closing_bracket[bracket]):
                    stacked_brackets.pop()
                else:
                    return False
            else:
                stacked_brackets.append(bracket)
        return not stacked_brackets


print(Solution().isValid("()") == True)
print(Solution().isValid("({})") == True)
print(Solution().isValid("(]") == False)
print(Solution().isValid("(})") == False)
print(Solution().isValid("([)") == False)
print(Solution().isValid("") == True)
print(Solution().isValid("[") == False)
