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
        for index in range(32):
            bit = (n >> index) & 1
            if bit:
                res += bit << (31 - index)
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
        bits = [0] * 32
        index = 0

        while n:
            bits[index] = n % 2
            n //= 2
            index += 1 
        
        res = 0
        for index, num in enumerate(reversed(bits)):
            if num:
                res += 2**index
        
        return res


print(Solution().reverseBits(43261596) == 964176192)
print(Solution().reverseBits(2147483644) == 1073741822)
