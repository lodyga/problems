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

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    def addNum(self, num: int) -> None:
        left = self.left_heap
        right = self.right_heap

        if len(left) == 0:
            heapq.heappush(left, -num)

        elif len(left) == len(right):
            if num <= right[0]:
                heapq.heappush(left, -num)
            else:
                heapq.heappush(left, -heapq.heappop(right))
                heapq.heappush(right, num)

        else:
            if num >= -left[0]:
                heapq.heappush(right, num)
            else:
                heapq.heappush(right, -heapq.heappop(left))
                heapq.heappush(left, -num)

    def findMedian(self) -> float:
        if len(self.left_heap) == len(self.right_heap):
            return (-self.left_heap[0] + self.right_heap[0]) / 2
        else:
            return -self.left_heap[0]


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
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
    ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"],
    ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
]

arguments_list = [
    [[], [1], [2], [], [3], []],
    [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []],
    [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []]
]

expected_output_list = [
    [None, None, None, 1.5, None, 2.0],
    [None, None, 6.00000, None, 8.00000, None, 6.00000, None, 6.00000, None, 6.00000, None, 5.50000, None, 6.00000, None, 5.50000, None, 5.00000, None, 4.00000, None, 3.00000],
    [None, None, -1.00000, None, -1.50000, None, -2.00000, None, -2.50000, None, -3.00000]
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


print(run_tests(operations_list, arguments_list, expected_output_list, show_output=False))


# Example 1
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian() == 1.5)
medianFinder.addNum(3)
print(medianFinder.findMedian() == 2)

