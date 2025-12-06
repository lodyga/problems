class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        if (
            k % 2 == 0 or
            k % 5 == 0
        ):
            return -1

        num = 0
        for index in range(1, k + 1):
            num = (num*10 + 1) % k
            if num % k == 0:
                return index

        return -1


print(Solution().smallestRepunitDivByK(1) == 1)
print(Solution().smallestRepunitDivByK(2) == -1)
print(Solution().smallestRepunitDivByK(3) == 3)
print(Solution().smallestRepunitDivByK(7) == 6)
print(Solution().smallestRepunitDivByK(149) == 148)
