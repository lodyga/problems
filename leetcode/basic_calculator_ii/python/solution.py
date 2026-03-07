class Solution:
    def calculate(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack, string
            A: iteration
        """
        stack = []
        num = 0
        is_digit = False

        # Convert string numbers to int numbers and push numbers and operators to stack.
        for char in text + " ":
            if char.isdigit():
                num *= 10
                num += int(char)
                is_digit = True
            elif is_digit:
                stack.append(num)
                is_digit = False
                num = 0

            if char in "+-*/":
                stack.append(char)

        equations = []
        index = 0
        # Handle // and * operators.
        while index < len(stack):
            char = stack[index]

            if char in ("*", "/"):
                index += 1

                if char == "/":
                    equations.append(equations.pop() // stack[index])
                else:
                    equations.append(equations.pop() * stack[index])
            else:
                equations.append(char)

            index += 1

        res = 0
        index = 0
        # Handle + and - operators.
        while index < len(equations):
            char = equations[index]

            if char in ("+", "-"):
                index += 1

                if char == "+":
                    res += equations[index]
                else:
                    res -= equations[index]
            else:
                res += char

            index += 1

        return res


print(Solution().calculate(" 0+0 ") == 0)
print(Solution().calculate(" 3/2 ") == 1)
print(Solution().calculate("3+2*2") == 7)
print(Solution().calculate(" 3+5 / 2 ") == 5)
print(Solution().calculate(" 50 / 10 ") == 5)
