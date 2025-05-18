class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        digit_stack = []

        for token in tokens:
            if token == "+":
                digit_stack.append(digit_stack.pop() + digit_stack.pop())
            elif token == "*":
                digit_stack.append((digit_stack.pop() * digit_stack.pop()))
            elif token == "-":
                digit_stack.append(-digit_stack.pop() + digit_stack.pop())
            elif token == "/":
                # 6 // -132 = -1; int(6 / -131) = 0
                digit_stack.append(int((1 / digit_stack.pop()) * digit_stack.pop()))
            try:
                digit_stack.append(int(token))
            except:
                pass
        
        return digit_stack[0]


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: recursion
        """

        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)

            b = dfs()
            a = dfs()

            if token == "+":
                return a + b
            elif token == "*":
                return a * b
            elif token == "-":
                return a - b
            elif token == "/":
                return int(a / b)

        return dfs()


print(Solution().evalRPN(["2", "1", "+", "3", "*"]), 9)
print(Solution().evalRPN(["4", "13", "5", "/", "+"]), 6)
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)
print(Solution().evalRPN(["18"]), 18)