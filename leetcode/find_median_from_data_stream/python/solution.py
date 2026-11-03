import heapq


class MedianFinder:
    """
    Time complexity:
        addNum: O(logn)
        findMedian: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: heap
        A: iteration
    """

    def __init__(self) -> None:
        # [x, ., ., ., .]
        self.high_heap = []
        # [-x, ., ., ., ,]
        self.low_heap = []

    def addNum(self, num: int) -> None:
        if len(self.high_heap) == len(self.low_heap):
            heapq.heappush(self.low_heap, -num)
            high_num = -heapq.heappop(self.low_heap)
            heapq.heappush(self.high_heap, high_num)
        else:
            heapq.heappush(self.high_heap, num)
            low_num = heapq.heappop(self.high_heap)
            heapq.heappush(self.low_heap, -low_num)

    def findMedian(self) -> float:
        if len(self.high_heap) == len(self.low_heap):
            return (self.high_heap[0] - self.low_heap[0]) / 2
        else:
            return self.high_heap[0]


def test_input(operations: list[str], arguments: list[list]) -> list[str | int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "MedianFinder":
            cls = MedianFinder(*argument)
            output.append(None)
        elif operation == "addNum":
            cls.addNum(*argument)
            output.append(None)
        elif operation == "findMedian":
            output.append(cls.findMedian(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"],
    ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian",
        "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
    ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum",
        "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
]

arguments_list = [
    [[], [1], [2], [], [3], []],
    [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0],
        [], [6], [], [3], [], [1], [], [0], [], [0], []],
    [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []]
]

expected_output_list = [
    [None, None, None, 1.5, None, 2.0],
    [None, None, 6.00000, None, 8.00000, None, 6.00000, None, 6.00000, None, 6.00000, None,
        5.50000, None, 6.00000, None, 5.50000, None, 5.00000, None, 4.00000, None, 3.00000],
    [None, None, -1.00000, None, -1.50000, None, -
        2.00000, None, -2.50000, None, -3.00000]
]


# Run tests
def run_tests(
        operations_list: list[list[str]],
        arguments_list: list[list[list[int]]],
        expected_output_list: list[list[int | None]],
        show_output: bool = False
) -> list[bool]:
    """
    Run a batch of TimeMap tests and compare outputs with expected results.
    If show_output is True, returns [(actual, expected), ...] instead of booleans.
    """
    output = []
    for operations, arguments, expected_output in zip(operations_list, arguments_list, expected_output_list):
        if show_output:
            output.append((test_input(operations, arguments), expected_output))
        else:
            output.append(test_input(operations, arguments) == expected_output)
    return output


print(run_tests(operations_list, arguments_list,
      expected_output_list, show_output=False))


# Example 1
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian() == 1.5)
medianFinder.addNum(3)
print(medianFinder.findMedian() == 2)
