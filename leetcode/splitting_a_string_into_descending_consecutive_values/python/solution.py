class Solution:
    def splitString(self, text: str) -> bool:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: backtracking with pruning
        """
        def backtrack(index: int, prev_num: int, is_valid: bool) -> bool:
            if index == len(text):
                return is_valid

            num = 0
            for end in range(index, len(text)):
                num = num*10 + int(text[end])

                if index == 0 or prev_num == num + 1:
                    if backtrack(end + 1, num, index != 0):
                        return True

            return False

        return backtrack(0, 0, False)


print(Solution().splitString("1") == False)
print(Solution().splitString("21") == True)
print(Solution().splitString("021") == True)
print(Solution().splitString("201") == True)
print(Solution().splitString("050043") == True)
print(Solution().splitString("0090089") == True)
print(Solution().splitString("001") == False)
print(Solution().splitString("9080701") == False)
print(Solution().splitString("1234") == False)
