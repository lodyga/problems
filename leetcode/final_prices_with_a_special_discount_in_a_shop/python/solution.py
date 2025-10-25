class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        monotonic increasing stack
        """
        stack = []
        discount_prices = []

        for price in reversed(prices):
            while stack and price < stack[-1]:
                stack.pop()
            
            discount_prices.append(price - (stack[-1] if stack else 0))
            stack.append(price)
            
        return list(reversed(discount_prices))


print(Solution().finalPrices([8, 4, 6, 2, 3]), [4, 2, 4, 2, 3])
print(Solution().finalPrices([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
print(Solution().finalPrices([10, 1, 1, 6]), [9, 0, 1, 6])
print(Solution().finalPrices([5, 4, 3, 2, 1]), [1, 1, 1, 1, 1])