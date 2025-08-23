class Solution:
    def convertToTitle(self, column_number: int) -> str:
        """
        Time complexity: O(logn)
            log (base = 26) n
        Auxiliary space complexity: O(1)
        Tags: string
        """
        column_name = ""

        while column_number > 0:
            mod = (column_number - 1) % 26
            column_name = chr(ord("A") + mod) + column_name
            column_number = (column_number - 1) // 26
        
        return column_name


print(Solution().convertToTitle(1) == "A")
print(Solution().convertToTitle(26) == "Z")
print(Solution().convertToTitle(28) == "AB")
print(Solution().convertToTitle(701) == "ZY")