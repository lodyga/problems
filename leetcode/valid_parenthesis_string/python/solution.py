class Solution:
    def checkValidString(self, text: str) -> bool:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: top-down
        """
        # [(index, opened parenthesis surplus]: is valid}
        memo = [[-1] * len(text) for _ in range(len(text))]

        def dfs(index: int, opened: int) -> int:
            if opened < 0:
                return 0
            elif index == len(text):
                return 1 if opened == 0 else 0
            elif memo[index][opened] != -1:
                return memo[index][opened]

            char = text[index]
            is_valid = False

            if char == "(":
                is_valid = dfs(index + 1, opened + 1)
            elif char == ")":
                is_valid = dfs(index + 1, opened - 1)
            elif char == "*":
                is_valid = dfs(index + 1, opened)
                is_valid |= dfs(index + 1, opened + 1)
                is_valid |= dfs(index + 1, opened - 1)

            memo[index][opened] = 1 if is_valid else 0
            return is_valid

        res = dfs(0, 0)
        return bool(res)


class Solution:
    def checkValidString(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        min_opened = 0
        max_opened = 0

        for char in text:
            if char == "(":
                min_opened += 1
                max_opened += 1
            
            elif char == ")":
                min_opened -= 1
                max_opened -= 1
            
            else:  # "*"
                min_opened -= 1
                max_opened += 1

            min_opened = max(min_opened, 0)
            if max_opened < 0:
                return False

        return min_opened == 0


print(Solution().checkValidString("*()") == True)
print(Solution().checkValidString(")") == False)
print(Solution().checkValidString("()") == True)
print(Solution().checkValidString("(*") == True)
print(Solution().checkValidString("(*)") == True)
print(Solution().checkValidString("(*))") == True)
print(Solution().checkValidString("(*)(") == False)
print(Solution().checkValidString("(*)*()") == True)
print(Solution().checkValidString("))(())") == False)
print(Solution().checkValidString("((*)*)*)((*") == False)
print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())") == False)
