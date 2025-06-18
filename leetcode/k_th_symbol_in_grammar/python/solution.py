r"""
draft
        0          1 = 2**0
       01          2 = 2**1
      0110         4 = 2**2
    01101001       8 = 2**3
0110100110010110
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(2^n)
        Tags: brute-force, mle
        """
        level = [0]
        for _ in range(n):
            for index in range(len(level)):
                if level[index] == 0:
                    level.append(1)
                else:
                    level.append(0)

        return level[k - 1]


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 1
        right = 2**(n - 1)
        val = 0

        while left < right:
            middle = (left + right) // 2

            if k <= middle:
                right = middle
            else:
                left = middle + 1
                val = 0 if val else 1
        
        return val


print(Solution().kthGrammar(1, 1) == 0)
print(Solution().kthGrammar(2, 1) == 0)
print(Solution().kthGrammar(2, 2) == 1)
print(Solution().kthGrammar(30, 434991989) == 0)