class FreqStack:
    """
    Time complexity: 
        O(1): push, pop
    Auxiliary space complexity: O(n)
    Tags:
        DS: hash map, list
        A: iteration
    """

    def __init__(self):
        # {value: frequency, ...}
        self.val_freq = {}
        # {frequency1: [value1, value2], ...}
        self.freq_bucket = []

    def push(self, val: int) -> None:
        idx = self.val_freq.get(val, 0)
        self.val_freq[val] = idx + 1

        if len(self.freq_bucket) == idx:
            self.freq_bucket.append([])

        self.freq_bucket[idx].append(val)

    def pop(self) -> int:
        if len(self.freq_bucket) == 0:
            return -1

        val = self.freq_bucket[-1].pop()
        
        if len(self.freq_bucket[-1]) == 0:
            self.freq_bucket.pop()
        
        self.val_freq[val] -= 1

        if self.val_freq[val] == 0:
            self.val_freq.pop(val)
        
        return val


def test_input(operations: list[str], arguments: list[list]) -> list[str | int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "FreqStack":
            cls = FreqStack(*argument)
            output.append(None)
        elif operation == "push":
            cls.push(*argument)
            output.append(None)
        elif operation == "pop":
            output.append(cls.pop(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["FreqStack", "push", "push", "push", "push",
        "push", "push", "pop", "pop", "pop", "pop"],
    ["FreqStack", "push", "push", "push", "push", "pop",
        "pop", "push", "push", "push", "pop", "pop", "pop"],
]

arguments_list = [
    [[], [5], [7], [5], [7], [4], [5], [], [], [], []],
    [[], [1], [1], [1], [2], [], [], [2], [2], [1], [], [], []],
]

expected_output_list = [
    [None, None, None, None, None, None, None, 5, 7, 5, 4],
    [None, None, None, None, None, 1, 1, None, None, None, 2, 1, 2],
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


print(run_tests(operations_list, arguments_list, expected_output_list))


# Example 1
freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop() == 5)
print(freqStack.pop() == 7)
print(freqStack.pop() == 5)
print(freqStack.pop() == 4)
