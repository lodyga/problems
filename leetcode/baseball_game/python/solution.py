class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        scores = []

        for operation in operations:
            if operation == 'C':
                scores.pop()
            elif operation == 'D':
                scores.append(scores[-1]*2)
            elif operation == '+':
                scores.append(scores[-2] + scores[-1])
            else:
                scores.append(int(operation))

        return sum(scores)


class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: iteration
        """
        scores = []

        for operation in operations:
            match operation:
                case 'C':
                    scores.pop()
                case 'D':
                    scores.append(scores[-1]*2)
                case '+':
                    scores.append(scores[-2] + scores[-1])
                case isdigit:
                    scores.append(int(operation))

        return sum(scores)


print(Solution().calPoints(["5", "2", "C", "D", "+"]) == 30)
print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27)
print(Solution().calPoints(["1", "C"]) == 0)
