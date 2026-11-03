class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: iteration
        """
        idx1 = len(a) - 1
        idx2 = len(b) - 1
        carry = False
        res = []

        while idx1 > -1 or idx2 > -1 or carry:
            char1 = a[idx1] if idx1 > -1 else '0'
            char2 = b[idx2] if idx2 > -1 else '0'

            if char1 == char2:
                res.append('1' if carry else '0')
                carry = char1 == '1'
            else:
                res.append('0' if carry else '1')

            idx1 -= 1
            idx2 -= 1

        return "".join(reversed(res))


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: iteration
        """
        idx1 = len(a) - 1
        idx2 = len(b) - 1
        carry = '0'
        res = []

        while idx1 > -1 and idx2 > -1:
            if a[idx1] == b[idx2]:
                res.append(carry)
                carry = a[idx1]
            else:
                res.append('1' if carry == '0' else '0')

            idx1 -= 1
            idx2 -= 1

        while idx1 > -1:
            if carry == a[idx1]:
                res.append('0')
                carry = a[idx1]
            else:
                res.append('1')
                carry = '0'

            idx1 -= 1

        while idx2 > -1:
            if carry == b[idx2]:
                res.append('0')
                carry = b[idx2]
            else:
                res.append('1')
                carry = '0'

            idx2 -= 1

        if carry == '1':
            res.append('1')
            carry = '0'

        return "".join(reversed(res))


print(Solution().addBinary("11", "1") == "100")
print(Solution().addBinary("1010", "1011") == "10101")
print(Solution().addBinary("11", "11") == "110")
print(Solution().addBinary("101111", "10") == "110001")
print(Solution().addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101", "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011") == "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000")
