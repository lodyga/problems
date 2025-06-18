class Solution:
    def splitString(self, text: str) -> bool:
        """
        Time complexity: O(n^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        def dfs(index: int, prev_value: int, parts: int) -> bool:
            if index == len(text):
                return parts > 1

            value = 0
            for index2 in range(index, len(text)):
                value = 10*value + int(text[index2])

                if ((
                    index == 0 or
                    prev_value - 1 == value
                ) and
                    dfs(index2 + 1, value, parts + 1)
                ):
                    return True

            return False
        return dfs(0, 0, 0)


print(Solution().splitString("1") == False)
print(Solution().splitString("21") == True)
print(Solution().splitString("021") == True)
print(Solution().splitString("201") == True)
print(Solution().splitString("050043") == True)
print(Solution().splitString("0090089") == True)
print(Solution().splitString("9080701") == False)
print(Solution().splitString("1234") == False)
print(Solution().splitString("001") == False)