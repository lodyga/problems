class Solution:
    def convertToTitle(self, col_num: int) -> str:
        """
        Time complexity: O(logn)
            log (base = 26) n
        Auxiliary space complexity: O(logn)
        Tags:
            DS: string
            A: iteration
        """
        col_name = []

        while col_num > 0:
            mod = (col_num - 1) % 26
            char = chr(ord("A") + mod)
            col_name.append(char)
            col_num = (col_num - 1) // 26

        return "".join(reversed(col_name))


print(Solution().convertToTitle(1) == "A")
print(Solution().convertToTitle(26) == "Z")
print(Solution().convertToTitle(27) == "AA")
print(Solution().convertToTitle(28) == "AB")
print(Solution().convertToTitle(51) == "AY")
print(Solution().convertToTitle(52) == "AZ")
print(Solution().convertToTitle(53) == "BA")
print(Solution().convertToTitle(54) == "BB")
print(Solution().convertToTitle(701) == "ZY")
print(Solution().convertToTitle(2147483647) == "FXSHRXW")
