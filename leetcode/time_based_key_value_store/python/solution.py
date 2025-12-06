from collections import deque


class TimeMap:
    """
    Time complexity: 
       set(): O(1)
       get(): O(n)
       n: `values assigned to a key` count
    Auxiliary space complexity: O(n*m)
        m: key count
    Tags:
        DS: queue, hash map
        A: iteration
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
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
       set(): O(1)
       get(): O(n)
       n: `values assigned to a key` count
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


class TimeMap:
    """
    Time complexity: 
       set(): O(1)
       get(): O(logn)
       n: `values assigned to a key` count
    Auxiliary space complexity: O(n*m)
        m: key count
    Tags:
        DS: list, hash map
        A: binary search
    """
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        store = self.store
        if key not in store:
            store[key] = [(0, "")]
        
        store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        store = self.store
        if key not in store:
            return ""

        key_vals = store[key]
        left = 0
        right = len(key_vals) - 1
        res = key_vals[right][1]

        while left <= right:
            middle = (left + right) >> 1
            middle_val = key_vals[middle]

            if timestamp == middle_val[0]:
                return middle_val[1]
            elif timestamp > middle_val[0]:
                res = middle_val[1]
                left = middle + 1
            else:
                right = middle - 1
        
        return res


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
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
    ["TimeMap","set","get","get","set","get","get"],
    ["TimeMap","set","set","get","get","get","get","get"],
    ["TimeMap","set","set","get","set","get","get"]
]

arguments_list = [
    [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]],
    [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]],
    [[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]
]

expected_output_list = [
    [None,None,"bar","bar",None,"bar2","bar2"],
    [None,None,None,"","high","high","low","low"],
    [None,None,None,"",None,"bar2","bar2"]
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
timeMap.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))  # return "bar"
print(timeMap.get("foo", 3))  # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4)  # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))  # return "bar2"
print(timeMap.get("foo", 5))  # return "bar2"

# Example 2
timeMap2 = TimeMap()
timeMap2.set("love", "high", 10)
timeMap2.set("love", "low", 20)
print(timeMap2.get("love", 5))  # return ""
print(timeMap2.get("love", 10))  # return high
print(timeMap2.get("love", 15))  # return high
print(timeMap2.get("love", 20))  # return low
print(timeMap2.get("love", 25))  # return low

# Example 3
timeMap3 = TimeMap()
timeMap3.set("a", "bar", 1)
timeMap3.set("x", "b", 3)
print(timeMap3.get("b", 3))  # return ""
timeMap3.set("foo", "bar2", 4)
print(timeMap3.get("foo", 4))  # return "bar2"
print(timeMap3.get("foo", 5))  # return "bar2"