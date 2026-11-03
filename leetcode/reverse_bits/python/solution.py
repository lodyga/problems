class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        mask = ['0'] * 32
        idx = 0

        for char in reversed(bin(n)[2:]):
            mask[idx] = char
            idx += 1

        return int("".join(mask), 2)


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        res = 0

        for idx in range(32):
            bit = (n >> idx) & 1

            if bit:
                res += bit << (31 - idx)

        return res


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Time complexity: O(1)
            O(32)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: bit manipulation
        """
        res = 0
        
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        
        return res


print(Solution().reverseBits(43261596) == 964176192)
print(Solution().reverseBits(2147483644) == 1073741822)




