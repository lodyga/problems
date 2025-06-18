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
    def numSquares(self, number: int) -> int:
        """
        Time complexity: O(nsqrtn)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        def get_perfect_squares(number):
            perfect_squares = []
            square_side = 1
            while square_side**2 <= number:
                perfect_squares.append(square_side**2)
                square_side += 1
            return perfect_squares
        
        perfect_squares = get_perfect_squares(number)
        cache = [number + 1] * (number + 1)
        cache[0] = 0

        for index in range(1, number + 1):
            if index in perfect_squares:
                cache[index] = 1
                continue
            
            for perfect_square in perfect_squares:
                if index - perfect_square >= 0:
                    cache[index] = min(cache[index], 
                                       cache[index - perfect_square] + 1)

        return cache[-1]


class Solution:
    def numSquares(self, number: int) -> int:
        """
        Time complexity: O(nsqrtn)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        def get_perfect_squares(number):
            perfect_squares = []
            square_side = 1
            while square_side**2 <= number:
                perfect_squares.append(square_side**2)
                square_side += 1
            return perfect_squares
        
        perfect_squares = get_perfect_squares(number)
        memo = {perfect_square: 1 
                for perfect_square in perfect_squares}

        def dfs(number):
            if number in memo:
                return memo[number]
            
            memo[number] = number + 1
            for perfect_square in perfect_squares:
                if number - perfect_square > 0:
                    memo[number] = min(memo[number], 
                                       dfs(number - perfect_square) + 1)

            return memo[number]

        dfs(number)
        return memo[number]


class Solution:
    def numSquares(self, number: int) -> int:
        """
        Time complexity: O(nsqrtn)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        def get_perfect_squares(number):
            perfect_squares = []
            square_side = 1
            while square_side**2 <= number:
                perfect_squares.append(square_side**2)
                square_side += 1
            return perfect_squares
        
        perfect_squares = get_perfect_squares(number)
        memo = [None] * (number + 1)
        
        for perfect_square in perfect_squares:
            memo[perfect_square] = 1

        def dfs(number):
            if memo[number] is not None:
                return memo[number]
            
            memo[number] = number + 1
            for perfect_square in perfect_squares:
                if number - perfect_square > 0:
                    memo[number] = min(memo[number], 
                                       dfs(number - perfect_square) + 1)

            return memo[number]

        dfs(number)
        return memo[number]


print(Solution().numSquares(1) == 1)  # 1
print(Solution().numSquares(9) == 1)  # 9
print(Solution().numSquares(16) == 1)  # 16
print(Solution().numSquares(2) == 2)  # 2 = 1 + 1
print(Solution().numSquares(5) == 2)  # 5 = 4 + 1
print(Solution().numSquares(13) == 2)  # 13 = 9 + 4
print(Solution().numSquares(12) == 3)  # 12 = 4 + 4 + 4
print(Solution().numSquares(7) == 4)  # 7 = 4 + 1 + 1 + 1
print(Solution().numSquares(28) == 4)  # 28 = 16 + 9 + 1 + 1 + 1 or 28 = 25 + 1 + 1 + 1
print(Solution().numSquares(43) == 3)  # 43 = 25 + 9 + 9