class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
        """
        discount_prices = prices.copy()
        stack = []

        for index, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                _, prev_index = stack.pop()
                discount_prices[prev_index] -= price

            stack.append((price, index))

        return discount_prices


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: monotonic increasing stack
        """
        stack = []

        for index, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                prev_index = stack.pop()
                prices[prev_index] -= prices[index]

            stack.append(index)

        return prices


print(Solution().finalPrices([8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3])
print(Solution().finalPrices([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5])
print(Solution().finalPrices([5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1])
print(Solution().finalPrices([10, 1, 1, 6]) == [9, 0, 1, 6])
