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
        def get_squares(num: int) -> list[int]:
            squares = [1]
            index = 2
            while squares[-1] < num:
                squares.append(index**2)
                index += 1
            if squares[-1] > num:
                squares.pop()
            squares.reverse()
            return squares

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
            squares = [1]
            index = 2
            while squares[-1] < num:
                squares.append(index**2)
                index += 1
            if squares[-1] > num:
                squares.pop()
            squares.reverse()
            return squares

        squares = get_squares(num)
        cache = [num + 1] * (num + 1)
        cache[-1] = 0

        for index in range(num - 1, -1, -1):
            for square in squares:
                if index + square > num:
                    continue
                cache[index] = min(cache[index], 1 + cache[index + square])

        return cache[0]


print(Solution().numSquares(1) == 1)
print(Solution().numSquares(2) == 2)
print(Solution().numSquares(9) == 1)
print(Solution().numSquares(16) == 1)
print(Solution().numSquares(5) == 2)
print(Solution().numSquares(13) == 2)
print(Solution().numSquares(12) == 3)
print(Solution().numSquares(7) == 4)
print(Solution().numSquares(28) == 4)
print(Solution().numSquares(43) == 3)
print(Solution().numSquares(204) == 3)
