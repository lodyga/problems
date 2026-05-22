class MyQueue:
    """
    Time complexity: O(1)
        push: O(1): push, pop, peek, empty
    Auxiliary space complexity: O(n)
    Tags:
        DS: stack, queue
        A: iteration
    """

    def __init__(self) -> None:
        self.stack = []
        self.rev_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def _reverse(self) -> None:
        if len(self.rev_stack) == 0:
            while self.stack:
                self.rev_stack.append(self.stack.pop())

    def peek(self) -> int:
        self._reverse()
        return self.rev_stack[-1]

    def pop(self) -> int:
        self._reverse()
        return self.rev_stack.pop()

    def empty(self) -> bool:
        return (
            len(self.stack) == 0 and
            len(self.rev_stack) == 0
        )


def test_input(operations: list[str], arguments: list[list]) -> list[str | int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "MyQueue":
            cls = MyQueue(*argument)
            output.append(None)
        elif operation == "push":
            cls.push(*argument)
            output.append(None)
        elif operation == "pop":
            output.append(cls.pop(*argument))
        elif operation == "peek":
            output.append(cls.peek(*argument))
        elif operation == "empty":
            output.append(cls.empty(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["MyQueue","push","push","peek","pop","empty"]
]

arguments_list = [
    [[],[1],[2],[],[],[]]
]

expected_output_list = [
    [None,None,None,1,1,False]
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


myQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek())  # return 1
print(myQueue.pop())  # return 1, queue is [2]
print(myQueue.empty())  # return false
