class FreqStack:
    """
    Time complexity: 
        O(1): push, pop
    Auxiliary space complexity: O(n)
    Tags: 
        DS: hash map
        A: iteration
    """

    def __init__(self):
        self.val_freq = {}  # {value: frequency, ...}
        self.freq_bucket = {}  # {frequency1: [value1, value2], ...}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.val_freq[val] = self.val_freq.get(val, 0) + 1

        freq = self.val_freq[val]
        if freq not in self.freq_bucket:
            self.freq_bucket[freq] = []
            self.max_freq = freq

        self.freq_bucket[freq].append(val)

    def pop(self) -> int:
        freq = self.max_freq
        val = self.freq_bucket[freq].pop()
        self.val_freq[val] -= 1

        if len(self.freq_bucket[freq]) == 0:
            self.freq_bucket.pop(freq)
            self.max_freq = freq - 1

        return val


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
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
