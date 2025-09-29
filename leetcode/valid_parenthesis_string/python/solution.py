class Solution:
    def checkValidString(self, text: str) -> bool:
        """
        Time complexity: O(3^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index, opened):
            if opened < 0:
                return False
            elif index == len(text):
                return opened == 0
            
            is_valid = False
            char = text[index]
            
            if char == "(":
                is_valid = dfs(index + 1, opened + 1)
            elif char == ")":
                is_valid = dfs(index + 1, opened - 1)
            elif char == "*":
                # blank char
                is_valid = dfs(index + 1, opened)
                # opening parent
                is_valid |= dfs(index + 1, opened + 1)
                # closing parent
                is_valid |= dfs(index + 1, opened - 1)

            return is_valid

        return dfs(0, 0)


class Solution:
    def checkValidString(self, text: str) -> bool:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {(index, opened parenthesis surplus): is valid}

        def dfs(index, opened):
            if opened < 0:
                return False
            elif index == len(text):
                return opened == 0
            elif (index, opened) in memo:
                return memo[(index, opened)]
            
            char = text[index]
            is_valid = False
            
            if char == "(":
                is_valid = dfs(index + 1, opened + 1)
            elif char == ")":
                is_valid = dfs(index + 1, opened - 1)
            elif char == "*":
                is_valid = (
                    # blank char
                    dfs(index + 1, opened) or
                    # opening parent
                    dfs(index + 1, opened + 1) or
                    # closing parent
                    dfs(index + 1, opened - 1)
                )

            memo[(index, opened)] = is_valid
            return is_valid

        return dfs(0, 0)


class Solution:
    def checkValidString(self, text: str) -> bool:
        max_opened = 0
        min_opened = 0
        
        for char in text:
            if char == "(":
                max_opened += 1
                min_opened += 1
            elif char == ")":
                max_opened -= 1
                min_opened -= 1
            elif char == "*":
                max_opened += 1
                min_opened -= 1

            if max_opened < 0:
                return False
            if min_opened < 0:
                min_opened = 0
        
        return min_opened == 0


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