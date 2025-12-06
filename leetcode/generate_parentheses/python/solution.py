class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: list
            A: backtracking
        """
        parenthesis = []
        parenthesis_list = []

        def backtrack(opened: int, closed: int) -> None:
            if opened + closed == 2*n:
                parenthesis_list.append("".join(parenthesis))
                return

            # open parenthesis
            if opened < n:
                parenthesis.append("(")
                backtrack(opened + 1, closed)
                parenthesis.pop()

            # close parenthesis
            if opened != closed:
                parenthesis.append(")")
                backtrack(opened, closed + 1)
                parenthesis.pop()

        backtrack(0, 0)
        return parenthesis_list


print(Solution().generateParenthesis(1) == ["()"])
print(Solution().generateParenthesis(2) == ["(())", "()()"])
print(Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"])
