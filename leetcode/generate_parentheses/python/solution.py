class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list, string
            A: backtracking
        """
        res = []
        parenthesis = []

        def backtrack(opened: int, closed: int) -> None:
            if opened == closed == n:
                res.append("".join(parenthesis))

            if opened < n:
                parenthesis.append("(")
                backtrack(opened + 1, closed)
                parenthesis.pop()

            if closed < opened:
                parenthesis.append(")")
                backtrack(opened, closed + 1)
                parenthesis.pop()

        backtrack(0, 0)
        return res


print(Solution().generateParenthesis(1) == ["()"])
print(Solution().generateParenthesis(2) == ["(())", "()()"])
print(Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"])
