r"""
draft
[1, 4, 9, 16, 25]
12 = 4 + 4 + 4 => 3
13 = 4 + 9 => 2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[   1  1  2  1  2  2  3  2  1           3]
[   1, 2,    4              9]
"""


class Solution:
    def numSquares(self, num: int) -> int:
        """
        Time complexity: O(n*sqrtn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: top-down
        """
        UPPER_BOUND = 2**31 - 1

        def get_squares(num: int) -> list[int]:
            nums = []
            n = 1
            square = n**2

            while square <= num:
                nums.append(square)
                n += 1
                square = n**2

            nums.reverse()
            return nums

        squares = get_squares(num)
        memo = {num: 1 for num in squares}
        memo[0] = 0

        def dfs(n: int) -> int:
            if n < 0:
                return UPPER_BOUND
            elif n in memo:
                return memo[n]

            res = UPPER_BOUND

            for square in squares:
                res = min(res, 1 + dfs(n - square))

            memo[n] = res
            return memo[n]

        dfs(num)
        return memo[num]


class Solution:
    def numSquares(self, num: int) -> int:
        """
        Time complexity: O(n*sqrtn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: top-down
        """
        def get_squares(num: int) -> list[int]:
            nums = []
            n = 1
            square = n**2

            while square <= num:
                nums.append(square)
                n += 1
                square = n**2

            nums.reverse()
            return nums

        squares = get_squares(num)
        memo = {num: 0}

        def dfs(total: int) -> int:
            if total > num:
                return num + 1
            elif total in memo:
                return memo[total]

            res = num + 1

            for square in squares:
                res = min(res, 1 + dfs(total + square))

            memo[total] = res
            return res

        return dfs(0)


class Solution:
    def numSquares(self, num: int) -> int:
        """
        Time complexity: O(n*sqrtn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: bottom-up
        """
        def get_squares(num: int) -> list[int]:
            nums = []
            n = 1
            square = n**2

            while square <= num:
                nums.append(square)
                n += 1
                square = n**2

            nums.reverse()
            return nums

        squares = get_squares(num)
        cache = [num + 1] * (num + 1)
        cache[num] = 0

        for n in range(num - 1, -1, -1):
            for square in squares:
                if (
                    n + square <= num 
                    and cache[n + square] < cache[n]
                ):
                    cache[n] = 1 + cache[n + square]

                # if n + square <= num:
                #     cache[n] = min(
                #         cache[n],
                #         1 + cache[n + square]
                #     )

        return cache[0]


print(Solution().numSquares(12) == 3)
print(Solution().numSquares(13) == 2)
print(Solution().numSquares(1) == 1)
print(Solution().numSquares(2) == 2)
print(Solution().numSquares(9) == 1)
print(Solution().numSquares(16) == 1)
print(Solution().numSquares(5) == 2)
print(Solution().numSquares(7) == 4)
print(Solution().numSquares(28) == 4)
print(Solution().numSquares(43) == 3)
print(Solution().numSquares(204) == 3)
