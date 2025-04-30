class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        number_stack = []

        for operation in operations:
            if operation == "C":
                number_stack.pop()
            elif operation == "D":
                number_stack.append(number_stack[-1] * 2)
            elif operation == "+":
                prev_number = number_stack.pop()
                last_number = prev_number + number_stack[-1]
                number_stack.extend((prev_number, last_number))
            else:
                try:
                    number_stack.append(int(operation))
                except:
                    pass

        return sum(number_stack)


print(Solution().calPoints(["5","2","C","D","+"]), 30)
print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]), 27)
print(Solution().calPoints(["1","C"]), 0)