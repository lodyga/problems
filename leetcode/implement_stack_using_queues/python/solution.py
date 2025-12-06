from collections import deque


class MyStack:
    """
    Time complexity:
        push: O(1)
        pop: O(n)
        top: O(n)
        empty: O(1)
    Auxiliary space complexity: O(n)
    Tags: 
        DS: queue, stack
        A: iteration
    """

    def __init__(self):
        self.queue = deque()

    def push(self, num: int) -> None:
        self.queue.append(num)

    def pop(self) -> int:
        queue = self.queue
        for _ in range(len(queue) - 1):
            queue.append(queue.popleft())
        return queue.popleft()

    def top(self) -> int:
        queue = self.queue
        for _ in range(len(queue) - 1):
            queue.append(queue.popleft())
        num = queue.popleft()
        queue.append(num)
        return num

    def empty(self) -> bool:
        return len(self.queue) == 0


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "MyStack":
            cls = MyStack(*argument)
            output.append(None)
        elif operation == "push":
            cls.push(*argument)
            output.append(None)
        elif operation == "pop":
            output.append(cls.pop(*argument))
        elif operation == "top":
            output.append(cls.top(*argument))
        elif operation == "empty":
            output.append(cls.empty(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["MyStack","push","push","top","pop","empty"]
]

arguments_list = [
    [[],[1],[2],[],[],[]]
]

expected_output_list = [
    [None,None,None,2,2,False]
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


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())  # return 2
print(myStack.pop())  # return 2
print(myStack.empty())  # return False
