class TimeMap:
    """
    Time complexity: 
       O(1): set
       O(logn): get
       n: key values count
    Auxiliary space complexity: O(n*m)
        m: key count
    Tags:
        DS: hash map
        A: binary search
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, val: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, val))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        stream = self.store[key]

        left = 0
        right = len(stream) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            mid_timestamp, mid_val = stream[mid]

            if timestamp == mid_timestamp:
                return mid_val
            elif timestamp < mid_timestamp:
                right = mid - 1
            else:
                res = mid_val
                left = mid + 1

        return res


class TimeMap:
    """
    Time complexity: 
       O(1): set
       O(n): get
       n: key values count
    Auxiliary space complexity: O(n*m)
        m: key count
    Tags:
        DS: queue, hash map
        A: iteration
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        from collections import deque
        store = self.store
        if key not in store:
            store[key] = deque([(0, "")])

        queue = store[key]
        queue.appendleft((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        store = self.store
        if key not in store:
            return ""

        queue = store[key]
        index = 0
        while timestamp < queue[index][0]:
            index += 1

        return queue[index][1]


class ListNode:
    def __init__(self, val=(0, ""), next=None) -> None:
        self.val = val  # (timestamp, value)
        self.next = next


class TimeMap:
    """
    Time complexity: 
       O(1): set
       O(n): get
       n: key values count
    Auxiliary space complexity: O(n*m)
        m: key count
    Tags:
        DS: linked list, hash map
        A: iteration
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        store = self.store
        if key not in store:
            store[key] = ListNode((0, ""))

        head = store[key]
        node = ListNode((timestamp, value), head)
        store[key] = node

    def get(self, key: str, timestamp: int) -> str:
        store = self.store
        if key not in store:
            return ""

        node = store[key]
        while timestamp < node.val[0]:
            node = node.next

        return node.val[1]


def test_input(type, operations: list[str], arguments: list[list]) -> list[str | int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "TimeMap":
            cls = TimeMap(*argument)
            output.append(None)
        elif operation == "set":
            cls.set(*argument)
            output.append(None)
        elif operation == "get":
            output.append(cls.get(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["TimeMap", "set", "get", "get", "set", "get", "get"],
    ["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
    ["TimeMap", "set", "set", "get", "set", "get", "get"]
]

arguments_list = [
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3],
        ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
    [[], ["love", "high", 10], ["love", "low", 20], ["love", 5],
        ["love", 10], ["love", 15], ["love", 20], ["love", 25]],
    [[], ["a", "bar", 1], ["x", "b", 3], ["b", 3],
        ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
]

expected_output_list = [
    [None, None, "bar", "bar", None, "bar2", "bar2"],
    [None, None, None, "", "high", "high", "low", "low"],
    [None, None, None, "", None, "bar2", "bar2"]
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
timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1) == "bar")
print(timeMap.get("foo", 3) == "bar")
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4) == "bar2")
print(timeMap.get("foo", 5) == "bar2")

# Example 2
timeMap2 = TimeMap()
timeMap2.set("love", "high", 10)
timeMap2.set("love", "low", 20)
print(timeMap2.get("love", 5) == "")
print(timeMap2.get("love", 10) == "high")
print(timeMap2.get("love", 15) == "high")
print(timeMap2.get("love", 20) == "low")
print(timeMap2.get("love", 25) == "low")

# Example 3
timeMap3 = TimeMap()
timeMap3.set("a", "bar", 1)
timeMap3.set("x", "b", 3)
print(timeMap3.get("b", 3) == "")
timeMap3.set("foo", "bar2", 4)
print(timeMap3.get("foo", 4) == "bar2")
print(timeMap3.get("foo", 5) == "bar2")
