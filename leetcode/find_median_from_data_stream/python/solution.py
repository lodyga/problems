import heapq


class MedianFinder:
    """
    Time complexity:
        addNum: O(logn)
        findMedian: O(1)
    Auxiliary space complexity: O(n)
    Tags: heap
    """

    def __init__(self):
        # max heap
        self.low_heap = []
        heapq.heapify(self.low_heap)
        # min heap
        self.high_heap = []
        heapq.heapify(self.high_heap)
        self.total_length = 0

    def addNum(self, number: int) -> None:
        # high heap is longer
        if self.total_length % 2:
            low_number = heapq.heappushpop(self.high_heap, number)
            heapq.heappush(self.low_heap, -low_number)
        else:
        # both heaps are equal lenght
            high_number = heapq.heappushpop(self.low_heap, -number)
            heapq.heappush(self.high_heap, -high_number)
        
        self.total_length += 1

    def findMedian(self) -> float:
        # high heap is longer
        if self.total_length % 2:
            return self.high_heap[0]
        # both heaps are equal lenght
        else:
            return (self.high_heap[0] - self.low_heap[0]) / 2


medianFinder = MedianFinder()
medianFinder.addNum(1)  # arr = [1]
medianFinder.addNum(2)  # arr = [1, 2]
print(medianFinder.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)  # arr[1, 2, 3]
print(medianFinder.findMedian())  # return 2.0


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
    Run a batch of MedianFinder tests and compare outputs with expected results.
    If show_output is True, returns [(actual, expected), ...] instead of booleans.
    """
    output = []
    for index, (operations, arguments, expected_output) in enumerate(zip(operations_list, arguments_list, expected_output_list), 1):
        if show_output:
            output.append((
                f"Test case {index} | " + 'PASS' if test_input(operations, arguments) == expected_output else 'FAIL',
                f"Test case {index} | Actual:   {test_input(operations, arguments)}",
                f"Test case {index} | Expected: {expected_output}",
                "="*150
            ))
        else:
            output.append(test_input(operations, arguments) == expected_output)
    return output

print(run_tests(operations_list, arguments_list, expected_output_list, show_output=False))1