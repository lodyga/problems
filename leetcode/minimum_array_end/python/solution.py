class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation, brute-force
        """
        num = x

        for _ in range(n - 1):
            num += 1
            num |= x
        return num


print(Solution().minEnd(3, 4) == 6)
print(Solution().minEnd(2, 7) == 15)
print(Solution().minEnd(3, 5) == 13)
print(Solution().minEnd(69735293, 5563569) == 142821814265)
print(Solution().minEnd(42076787, 25326514) == 172363546550)
