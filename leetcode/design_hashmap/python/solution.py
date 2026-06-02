class ListNode:
    def __init__(self, key=None, val=None, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode()

    def set(self, key: int, val: int) -> None:
        node = self.head

        while node.next:
            if node.next.key == key:
                node.next.val = val
                return
            node = node.next

        node.next = ListNode(key, val)

    def has(self, key: int) -> bool:
        node = self.head

        while node.next:
            if node.next.key == key:
                return True
            node = node.next

        return False

    def get(self, key: int) -> int:
        node = self.head

        while node.next:
            if node.next.key == key:
                return node.next.val
            node = node.next

        return -1

    def discard(self, key: int) -> None:
        node = self.head

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


class MyHashMap:
    """
    Time complexity:
        constructor: O(n)
        put: O(1)
        get: O(1)
        remove: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: linked list, hash map
        A: iteration
    """

    CAPACITY = 10**4

    def __init__(self) -> None:
        self.buckets = [LinkedList() for _ in range(self.CAPACITY)]

    def _get_hash_key(self, key: int) -> int:
        return key % self.CAPACITY

    def _get_linked_list(self, key: int) -> LinkedList:
        hash_key = self._get_hash_key(key)
        return self.buckets[hash_key]

    def put(self, key: int, val: int) -> None:
        linked_list = self._get_linked_list(key)
        linked_list.set(key, val)

    def get(self, key: int) -> int:
        linked_list = self._get_linked_list(key)
        return linked_list.get(key)

    def remove(self, key: int) -> None:
        linked_list = self._get_linked_list(key)
        linked_list.discard(key)

    def contains(self, key: int) -> bool:
        linked_list = self._get_linked_list(key)
        return linked_list.has(key)


class MyHashMap:
    """
    Time complexity:
        constructor: O(n)
        put: O(1)
        get: O(1)
        remove: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: list, hash map
        A: iteration
    """

    CAPACITY = 10**4

    def __init__(self) -> None:
        self.buckets = [[] for _ in range(self.CAPACITY)]

    def _get_hash_key(self, key: int) -> int:
        return key % self.CAPACITY

    def _get_list(self, key: int) -> list:
        hash_key = self._get_hash_key(key)
        return self.buckets[hash_key]

    def _get_index(self, key: int) -> int:
        bucket = self._get_list(key)

        try:
            keys = [key for key, _ in bucket]
            idx = keys.index(key)
        except ValueError:
            idx = -1

        return idx

    def put(self, key: int, val: int) -> None:
        bucket = self._get_list(key)
        idx = self._get_index(key)

        if idx == -1:
            bucket.append((key, val))
        else:
            bucket[idx] = (key, val)

    def get(self, key: int) -> int:
        idx = self._get_index(key)

        if idx == -1:
            return -1

        bucket = self._get_list(key)
        return bucket[idx][1]

    def remove(self, key: int) -> None:
        idx = self._get_index(key)

        if idx != -1:
            bucket = self._get_list(key)
            bucket.pop(idx)

    def contains(self, key: int) -> bool:
        return self._get_index(key) != -1


def test_input(operations: list[str], arguments: list[list]) -> list[str | int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "MyHashMap":
            cls = MyHashMap(*argument)
            output.append(None)
        elif operation == "put":
            cls.put(*argument)
            output.append(None)
        elif operation == "remove":
            cls.remove(*argument)
            output.append(None)
        elif operation == "get":
            output.append(cls.get(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
]

arguments_list = [
    [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
]

expected_output_list = [
    [None, None, None, 1, -1, None, 1, None, -1]
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
myHashMap = MyHashMap()
myHashMap.put(1, 1)  # The map is now [[1,1]]
myHashMap.put(2, 2)  # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))  # return 1, The map is now [[1,1], [2,2]]
# return -1 (i.e., not found), The map is now [[1,1], [2,2]]
print(myHashMap.get(3))
myHashMap.put(2, 1)  # The map is now [[1,1], [2,1]]
print(myHashMap.get(2))  # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2)  # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))  # return -1 (i.e., not found), The map is now [[1,1]]
