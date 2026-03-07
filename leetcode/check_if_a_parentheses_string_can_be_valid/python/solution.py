class Solution:
    def canBeValid(self, text: str, locked: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        if len(text) % 2 == 1:
            return False

        min_opened = 0
        max_opened = 0

        for p, b in zip(text, locked):
            if b == "0":
                min_opened -= 1
                max_opened += 1
            elif p == "(":
                min_opened += 1
                max_opened += 1
            elif p == ")":
                min_opened -= 1
                max_opened -= 1

            if max_opened < 0:
                return False

            min_opened = max(min_opened, 0)

        return min_opened == 0


print(Solution().canBeValid("()", "11") == True)
print(Solution().canBeValid("))()))", "010100") == True)
print(Solution().canBeValid("()()", "0000") == True)
print(Solution().canBeValid(")", "0") == False)
print(Solution().canBeValid("(((())", "111111") == False)
print(Solution().canBeValid("(((())(((())", "111111010111") == True)
print(Solution().canBeValid("()()((()))((", "111111101101") == False)
