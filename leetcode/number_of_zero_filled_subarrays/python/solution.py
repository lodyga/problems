class Solution:    
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: math, iteration
            Arithmetic series.
        """
        nums.append(-1)
        zeros = 0
        res = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                res += (1 + zeros) * zeros // 2
                zeros = 0

        nums.pop()
        return res


class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: math, iteration
        """
        zeros = 0
        res = 0

        for num in nums:
            if num == 0:
                zeros += 1
            else:
                zeros = 0

            res += zeros

        return res


print(Solution().zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6)
print(Solution().zeroFilledSubarray([0, 0, 0, 2, 0, 0]) == 9)
print(Solution().zeroFilledSubarray([2, 10, 2019]) == 0)
