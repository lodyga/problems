class MinStack:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: stack
        A: iteration
    """

    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


def test_input(cls, operations: list[str], arguments: list[list]) -> list[str | int | None]:
    res = []

    for operation, argument in zip(operations, arguments):
        # Constructor
        if operation == cls.__name__:
            instance = cls(*argument)
            res.append(None)
            continue

        # Method call
        method = getattr(instance, operation)
        result = method(*argument)
        res.append(result)

    return res


# Example Input
operations_list = [
    ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
]

arguments_list = [
    [[], [-2], [0], [-3], [], [], [], []],
]

expected_output_list = [
    [None, None, None, None, -3, None, 0, -2]
]


# Run tests
def run_tests(
        cls,
        operations_list: list[list[str]],
        arguments_list: list[list[list[int]]],
        expected_output_list: list[list[int | None]],
        show_output: bool = False
) -> list[bool]:
    """
    Run a batch of TimeMap tests and compare outputs with expected results.
    If show_output is True, returns [(actual, expected), ...] instead of booleans.
    """
    res = []

    for operations, arguments, expected_output in zip(operations_list, arguments_list, expected_output_list):
        if show_output:
            res.append((
                test_input(
                    cls,
                    operations,
                    arguments
                ),
                expected_output
            )
            )
        else:
            res.append(
                test_input(
                    cls,
                    operations,
                    arguments
                ) == expected_output
            )

    return res


print(run_tests(MinStack, operations_list, arguments_list, expected_output_list))


# Example 1
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin() == -3)
minStack.pop()
print(minStack.top() == 0)
print(minStack.getMin() == -2)
