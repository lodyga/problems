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
        Tags: 
            A: brute-force
        """
        bins = [0]

        for _ in range(1, n):
            for col in range(len(bins)):
                bins.append(0 if bins[col] else 1)

        return bins[k - 1]


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: binary search
        """
        k -= 1
        left = 0
        right = 2**(n - 1) - 1
        res = 0

        while left < right:
            mid = (left + right) // 2

            if k <= mid:
                right = mid
            else:
                res = 0 if res else 1
                left = mid + 1

        return res


print(Solution().kthGrammar(1, 1) == 0)
print(Solution().kthGrammar(2, 1) == 0)
print(Solution().kthGrammar(2, 2) == 1)
print(Solution().kthGrammar(30, 434991989) == 0)
