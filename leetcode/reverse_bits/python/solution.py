class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time complexity: O(1)
            O(32) => O(1)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        bin_short = bin(n)[2:]
        leading_zeros =  (32 - len(bin_short)) * "0"
        bin_full = leading_zeros + bin_short
        return int(bin_full[::-1], 2)

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time complexity: O(1)
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res


print(Solution().reverseBits(43261596) == 964176192)
print(Solution().reverseBits(2147483644) == 1073741822)