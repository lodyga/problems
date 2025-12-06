class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: stack
            A: iteration
        """
        num_stack = []

        for operation in operations:
            if operation == "C":
                num_stack.pop()
            elif operation == "D":
                num_stack.append(num_stack[-1] * 2)
            elif operation == "+":
                num_stack.append(num_stack[-2] + num_stack[-1])
            else:
                num_stack.append(int(operation))

        return sum(num_stack)


print(Solution().calPoints(["5", "2", "C", "D", "+"]) == 30)
print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27)
print(Solution().calPoints(["1", "C"]) == 0)
