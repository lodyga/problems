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
    def integerBreak(self, num: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: array
            A: top-down
        """
        # [number: product] maximum product for current number
        # [0: 1] When the number is partitioned (rest = 0) it is multiplied by 1
        memo = [-1] * (num + 1)
        memo[0] = 1

        def dfs(num, is_valid):
            if memo[num] != -1:
                return memo[num]

            res = 0
            for digit in range(1, num + is_valid):
                res = max(res, digit * dfs(num - digit, True))

            memo[num] = res
            return res

        return dfs(num, False)


print(Solution().integerBreak(2) == 1)
print(Solution().integerBreak(3) == 2)
print(Solution().integerBreak(4) == 4)
print(Solution().integerBreak(5) == 6)
print(Solution().integerBreak(6) == 9)
print(Solution().integerBreak(7) == 12)
print(Solution().integerBreak(10) == 36)
print(Solution().integerBreak(24) == 6561)
