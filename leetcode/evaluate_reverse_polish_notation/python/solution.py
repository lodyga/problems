class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        num_stack = []
        for token in tokens:
            if token == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif token == "-":
                num_stack.append(-num_stack.pop() + num_stack.pop())
            elif token == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif token == "/":
                num_stack.append(int(1/num_stack.pop() * num_stack.pop()))
            else:
                num_stack.append(int(token))
        return num_stack[0]


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: recursion
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


print(Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9)
print(Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6)
print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22)
print(Solution().evalRPN(["18"]) == 18)
