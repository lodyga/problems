class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: iteration
        """
        index1 = len(a) - 1
        index2 = len(b) - 1
        res = []
        carry = False

        while index1 > -1 or index2 > -1 or carry:
            num1 = a[index1] if index1 > -1 else "0"
            num2 = b[index2] if index2 > -1 else "0"

            if num1 == num2 == "0":
                res.append("1") if carry else res.append("0")
                carry = False
            elif num1 == num2 == "1":
                res.append("1") if carry else res.append("0")
                carry = True
            else:
                res.append("0") if carry else res.append("1")

            index1 -= 1
            index2 -= 1

        return "".join(reversed(res))


print(Solution().addBinary("11", "1") == "100")
print(Solution().addBinary("1010", "1011") == "10101")
print(Solution().addBinary("11", "11") == "110")
