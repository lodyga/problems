r"""
draft
                        4
                  1/            2|           3\  
                  3              2            1
               1/     2\        1/ \2        1|
              2       1        1     0        0
           1/  \2    1|       1|
           1    0     1        0
          1|
           0

"""


class Solution:
    def integerBreak(self, number: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        # {number: product}  maximum product for current number
        # {0: 1} When the number is partitioned (rest = 0) it is multiplied by 1
        memo = {0: 1}

        def dfs(number, is_two_part):
            if number in memo:
                return memo[number]

            memo[number] = 0

            for digit in range(1, number + int(is_two_part)):
                memo[number] = max(memo[number], 
                                  digit * dfs(number - digit, True))
            
            return memo[number]
        
        return dfs(number, False)


class Solution:
    def integerBreak(self, number: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as array
        """
        # {number: product}  maximum product for current number
        # {0: 1} When the number is partitioned (rest = 0) it is multiplied by 1
        memo = [None] * (number + 1)
        memo[0] = 1

        def dfs(number, is_two_part):
            if memo[number] is not None:
                return memo[number]

            memo[number] = 0

            for digit in range(1, number + int(is_two_part)):
                memo[number] = max(memo[number], 
                                  digit * dfs(number - digit, True))
            
            return memo[number]
        
        return dfs(number, False)


class Solution:
    def integerBreak(self, number: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        """
        # {0: 1} When the number is partitioned (rest = 0) it is multiplied by 1

        def dfs(number, is_two_part):
            if number == 0:
                return 1

            memo = 0

            for digit in range(1, number + int(is_two_part)):
                memo = max(memo, 
                                  digit * dfs(number - digit, True))
            
            return memo
        
        return dfs(number, False)


class Solution:
    def integerBreak(self, number: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        # {number: product}  maximum product for current number
        # {0: 1} When the number is partitioned (rest = 0) it is multiplied by 1
        memo = [None] * (number + 1)
        memo[0] = 1

        def dfs(number, is_two_part):
            if memo[number] is not None:
                return memo[number]

            memo[number] = 0

            for digit in range(1, number + int(is_two_part)):
                memo[number] = max(memo[number], 
                                  digit * dfs(number - digit, True))
            
            return memo[number]
        
        return dfs(number, False)


print(Solution().integerBreak(2) == 1)  # Explanation: 2 = 1 + 1, 1 × 1 = 1.
print(Solution().integerBreak(3) == 2)  # Explanation: 3 = 1 + 2, 1 × 2 = 2.
print(Solution().integerBreak(4) == 4)  # Explanation: 4 = 2 + 2, 2 × 2 = 4.
print(Solution().integerBreak(5) == 6)  # Explanation: 5 = 2 + 3, 2 × 3 = 6.
print(Solution().integerBreak(6) == 9)  # Explanation: 6 = 3 + 3, 3 × 3 = 9.
print(Solution().integerBreak(7) == 12)  # Explanation: 7 = 3 + 4, 3 × 4 = 12; 2 = 2 + 2 + 3, 2 x 2 x 3 = 12.
print(Solution().integerBreak(10) == 36)  # Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
print(Solution().integerBreak(24) == 6561)  # tle testcase


class Solution:
    def integerBreak(self, n: int) -> int:
        """
        O(2^n), O(n)
        brute force, backtracking, tle
        """
        integers = []
        max_product = 0

        def product():
            p = 1
            for number in integers:
                p *= number
            return p

        def dfs(n, max_product):
            if (n == 0 and
                    len(integers) > 1):
                max_product = max(max_product, product())
                return max_product

            for index in range(1, n + 1):
                integers.append(index)
                max_product = dfs(n - index, max_product)
                integers.pop()
            
            return max_product

        return dfs(n, max_product)