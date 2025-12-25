class StockSpanner:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: monotonic decreasing stack
        A: iteration
    """

    def __init__(self):
        # monotonic decreasing stack
        # [(price, span), ...]
        self.prices = []

    def next(self, price: int) -> int:
        prices = self.prices
        span = 1

        while prices and prices[-1][0] <= price:
            _, prev_span = prices.pop()
            span += prev_span
        prices.append((price, span))

        return span


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "StockSpanner":
            cls = StockSpanner(*argument)
            output.append(None)
        elif operation == "next":
            output.append(cls.next(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
]

arguments_list = [
    [[], [100], [80], [60], [70], [60], [75], [85]]
]

expected_output_list = [
    [None, 1, 1, 1, 2, 1, 4, 6]
]


# Run tests
def run_tests(
        operations_list: list[list[str]],
        arguments_list: list[list[list[int]]],
        expected_output_list: list[list[int | None]],
        show_output: bool = False
) -> list[bool]:
    """
    Run a batch of StockSpanner tests and compare outputs with expected results.
    If show_output is True, returns [(actual, expected), ...] instead of booleans.
    """
    output = []
    for operations, arguments, expected_output in zip(operations_list, arguments_list, expected_output_list):
        if show_output:
            output.append((test_input(operations, arguments), expected_output))
        else:
            output.append(test_input(operations, arguments) == expected_output)
    return output


print(run_tests(operations_list, arguments_list, expected_output_list))


# Example 1
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # return 1
print(stockSpanner.next(80))  # return 1
print(stockSpanner.next(60))  # return 1
print(stockSpanner.next(70))  # return 2
print(stockSpanner.next(60))  # return 1
# return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
print(stockSpanner.next(75))
print(stockSpanner.next(85))  # return 6
