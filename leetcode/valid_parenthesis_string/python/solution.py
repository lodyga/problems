class Solution:
    def checkValidString(self, text: str) -> bool:
        """
        Time complexity: O(3^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        def dfs(index, opened, closed):
            if opened < closed:
                return False
            elif index == len(text):
                return opened == closed

            char = text[index]

            if char == "(":
                return dfs(index + 1, opened + 1, closed)

            elif char == ")":
                if opened == closed:
                    return False
                else:
                    return dfs(index + 1, opened, closed + 1)

            elif char == "*":
                return (
                    # blank char
                    dfs(index + 1, opened, closed) or
                    # opening parent
                    dfs(index + 1, opened + 1, closed) or
                    # closing parent
                    dfs(index + 1, opened, closed + 1)
                )
            
        return dfs(0, 0, 0)


class Solution:
    def checkValidString(self, text: str) -> bool:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {(index, opened, closed): bool}

        def dfs(index, opened, closed):
            if opened < closed:
                return False
            elif index == len(text):
                return opened == closed
            elif (index, opened, closed) in memo:
                return memo[(index, opened, closed)]

            char = text[index]

            if char == "(":
                memo[(index, opened, closed)] = dfs(index + 1, opened + 1, closed)

            elif char == ")":
                if opened == closed:
                    return False
                else:
                    memo[(index, opened, closed)] = dfs(index + 1, opened, closed + 1)

            elif char == "*":
                memo[(index, opened, closed)] = (
                    # blank char
                    dfs(index + 1, opened, closed) or
                    # opening parent
                    dfs(index + 1, opened + 1, closed) or
                    # closing parent
                    dfs(index + 1, opened, closed + 1)
                )
            
            return memo[(index, opened, closed)]

        return dfs(0, 0, 0)


class Solution:
    def checkValidString(self, text: str) -> bool:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {}  # {(index, opened): bool}

        def dfs(index, opened):
            if opened < 0:
                return False
            elif index == len(text):
                return opened == 0
            elif (index, opened) in memo:
                return memo[(index, opened)]

            char = text[index]

            if char == "(":
                memo[(index, opened)] = dfs(index + 1, opened + 1)

            elif char == ")":
                if opened == 0:
                    return False
                else:
                    memo[(index, opened)] = dfs(index + 1, opened - 1)

            elif char == "*":
                memo[(index, opened)] = (
                    # blank char
                    dfs(index + 1, opened) or
                    # opening parent
                    dfs(index + 1, opened + 1) or
                    # closing parent
                    dfs(index + 1, opened - 1)
                )
            
            return memo[(index, opened)]

        return dfs(0, 0)


class Solution:
    def checkValidString(self, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: gredy
        """
        open_min = open_max = 0

        for char in text:
            if char == "(":
                open_min += 1
                open_max += 1
            elif char == ")":
                open_min -= 1
                open_max -= 1
            else:
                open_min -= 1
                open_max += 1
            
            open_min = max(0, open_min)
            if open_max < 0:
                return False
        
        return open_min == 0


print(Solution().checkValidString(")") == False)
print(Solution().checkValidString("()") == True)
print(Solution().checkValidString("(*") == True)
print(Solution().checkValidString("(*)") == True)
print(Solution().checkValidString("(*))") == True)
print(Solution().checkValidString("(*)(") == False)
print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())") == False)
print(Solution().checkValidString("((*)*)*)((*") == False)