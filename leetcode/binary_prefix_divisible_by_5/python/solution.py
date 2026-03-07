class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: bit manipulation
        """
        val = 0
        res = []

        for num in nums:
            val <<= 1
            val += num
            res.append(False if val % 5 else True)

        return res


class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: bit manipulation
        """
        val = 0
        res = []

        for num in nums:
            val = (val * 2 + num) % 5
            res.append(val == 0)

        return res


print(Solution().prefixesDivBy5([1, 0, 1]) == [False, False, True])
print(Solution().prefixesDivBy5([0, 1, 1]) == [True, False, False])
print(Solution().prefixesDivBy5([1, 1, 1]) == [False, False, False])
print(Solution().prefixesDivBy5([0, 1, 1, 1, 1, 1]) == [True, False, False, False, True, False])
print(Solution().prefixesDivBy5([1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1]) == [False, False, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False])
