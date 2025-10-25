class StockSpanner:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags: stack, monotonic stack
    monotonic decreasing stack
    """

    def __init__(self):
        self.prices_stack = []
        self.index = 0

    def next(self, price: int) -> int:
        span = 1
        prev_index = self.index
        
        while self.prices_stack and self.prices_stack[-1][1] <= price:
            prev_index, _ = self.prices_stack.pop()
            span = self.index - prev_index + 1
        
        self.prices_stack.append((prev_index, price))
        self.index += 1
        return span


class StockSpanner:
    """
    Time complexity: O(n2)
    Auxiliary space complexity: O(n)
    Tags: brute-force
    """

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        counter = 0

        for current_price in reversed(self.prices):
            if price < current_price:
                break

            counter += 1

        return counter


class StockSpanner:
    """
    Time complexity: O(n2)
    Auxiliary space complexity: O(n)
    Tags: brute-force
    """

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        counter = 0
        right = len(self.prices) - 1

        while (right >= 0 and
               price >= self.prices[right]):
            counter += 1
            right -= 1

        return counter


stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # return 1
print(stockSpanner.next(80))  # return 1
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(70))  # return 2
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(75))  # return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
print(stockSpanner.next(85))  # return 6