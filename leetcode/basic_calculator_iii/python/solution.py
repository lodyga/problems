class Solution:
    def calculate(self, s: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: iteration
        """
        def eval_multi(arr):
            """Eval * and /."""
            index = 0
            res = []

            while index < len(arr):
                char = arr[index]
                if char == "/":
                    res.append(res.pop() // arr[index + 1])
                    index += 1
                elif char == "*":
                    res.append(res.pop() * arr[index + 1])
                    index += 1
                else:
                    res.append(char)
                index += 1

            return res

        def eval_add(arr):
            """Eval + and -."""
            index = 1
            res = arr[0]

            while index < len(arr):
                char = arr[index]
                if char == "+":
                    res += arr[index + 1]
                    index += 1
                elif char == "-":
                    res -= arr[index + 1]
                    index += 1
                index += 1

            return res

        # Parse ints, operations and parenths.
        num = 0
        is_num = False
        stack = []
        for char in s + " ":
            if char.isdigit():
                num = num * 10 + int(char)
                is_num = True
                continue
            elif is_num:
                stack.append(num)
                num = 0
                is_num = False

            if char in "*/+-()":
                stack.append(char)

        # Eval parenths.
        arr = []
        chunk = []
        add_chunk = False
        for char in stack:
            if char == "(":
                add_chunk = True
                continue
            elif char == ")":
                add_chunk = False

            if add_chunk:
                chunk.append(char)
                continue

            if not add_chunk and chunk:
                multi_evaled = eval_multi(chunk)
                add_evaled = eval_add(multi_evaled)
                arr.append(add_evaled)
                chunk.clear()
            else:
                arr.append(char)

        multi_evaled = eval_multi(arr)
        add_evaled = eval_add(multi_evaled)
        return add_evaled


print(Solution().calculate("1+1") == 2)
print(Solution().calculate("13+31") == 44)
print(Solution().calculate("6-4/2") == 4)
print(Solution().calculate("6/4+2") == 3)
print(Solution().calculate("(6-4)/2") == 1)
print(Solution().calculate("2*(5+5*2)/3+(6/2+8)") == 21)
print(Solution().calculate("2*((5+5)/2)+3") == 13)
print(Solution().calculate("2*(3+(4*5))") == 46)
print(Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23)
print(Solution().calculate("3-5/2") == 1)
