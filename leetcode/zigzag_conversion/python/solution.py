class Solution:
    def convert(self, text: str, num_rows: int) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string, array
            A: iteration
        """
        if num_rows == 1:
            return text

        res = [""] * num_rows

        for index, letter in enumerate(text):
            row = index % (2*(num_rows - 1))

            if row < num_rows:
                new_index = row
            else:
                new_index = 2*(num_rows - 1) - row

            res[new_index] = res[new_index] + letter

        return "".join(res)


print(Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
print(Solution().convert("A", 1) == "A")
