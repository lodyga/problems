class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        stack = []

        for operation in operations:
            match operation:
                case "C":
                    stack.pop()
                case "D":
                    stack.append(stack[-1] * 2)
                case "+":
                    stack.append(stack[-2] + stack[-1])
                case isdigit:
                    stack.append(int(operation))

        return sum(stack)


print(Solution().calPoints(["5", "2", "C", "D", "+"]) == 30)
print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27)
print(Solution().calPoints(["1", "C"]) == 0)
