class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        parenthesis = []
        parenthesisList = []
        
        def dfs(open, close):
            if open == 0 and close == 0:
                parenthesisList.append("".join(parenthesis))
                return
            
            if open:
                parenthesis.append("(")
                dfs(open - 1, close)
                parenthesis.pop()
            if close > open:
                parenthesis.append(")")
                dfs(open, close - 1)
                parenthesis.pop()
        
        dfs(n, n)
        return parenthesisList


print(Solution().generateParenthesis(1), ["()"])
print(Solution().generateParenthesis(2), ["(())", "()()"])
print(Solution().generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])