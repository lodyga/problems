class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        res = 0
        prev_prive = prices[0]

        for price in prices:
            if price > prev_prive:
                res += price - prev_prive

            prev_prive = price

        return res


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7)
print(Solution().maxProfit([1, 2, 3, 4, 5]) == 4)
print(Solution().maxProfit([7, 6, 4, 3, 1]) == 0)
print(Solution().maxProfit([7, 1]) == 0)
print(Solution().maxProfit([1, 7]) == 6)
