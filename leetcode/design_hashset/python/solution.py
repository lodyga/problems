class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode()

    def add(self, val: int) -> None:
        node = self.head

        while node.next:
            if node.next.val == val:
                return
            node = node.next

        node.next = ListNode(val)

    def has(self, val: int) -> bool:
        node = self.head

        while node.next:
            if node.next.val == val:
                return True
            node = node.next

        return False

    def discard(self, val: int) -> None:
        node = self.head

        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                return
            node = node.next


class MyHashSet:
    """
    Time complexity:
        constructor: O(CAPACITY)
        add: avg O(1)
        contains: avg O(1)
        remove: avg O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: linked list, hash set
        A: iteration
    """

    CAPACITY = 10**4

    def __init__(self) -> None:
        self.buckets = [LinkedList() for _ in range(self.CAPACITY)]

    def _get_hash_key(self, val: int) -> int:
        return val % self.CAPACITY
    
    def _get_linked_list(self, val: int) -> LinkedList:
        hash_key = self._get_hash_key(val)
        return self.buckets[hash_key]

    def add(self, val: int) -> None:
        linked_list = self._get_linked_list(val)
        linked_list.add(val)

    def contains(self, val: int) -> bool:
        linked_list = self._get_linked_list(val)
        return linked_list.has(val)

    def remove(self, val: int) -> None:
        linked_list = self._get_linked_list(val)
        linked_list.discard(val)


class MyHashSet:
    """
    Time complexity:
        constructor: O(CAPACITY)
        add: avg O(1)
        contains: avg O(1)
        remove: avg O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: list, hash set
        A: iteration
    """

    CAPACITY = 10**4

    def __init__(self) -> None:
        self.buckets = [[] for _ in range(self.CAPACITY)]

    def _get_hash_key(self, val: int) -> int:
        return val % self.CAPACITY

    def _get_list(self, val: int) -> list:
        hash_key = self._get_hash_key(val)
        return self.buckets[hash_key]

    def _get_index(self, val: int) -> int:
        bucket = self._get_list(val)

        try:
            idx = bucket.index(val)
        except ValueError:
            idx = -1

        return idx

    def add(self, val: int) -> None:
        if not self.contains(val):
            bucket = self._get_list(val)
            bucket.append(val)

    def contains(self, val: int) -> bool:
        return self._get_index(val) != -1

    def remove(self, val: int) -> None:
        idx = self._get_index(val)

        if idx != -1:
            bucket = self._get_list(val)
            bucket.pop(idx)


def test_input(operations: list[str], arguments: list[list]) -> list[str | int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "MyHashSet":
            cls = MyHashSet(*argument)
            output.append(None)
        elif operation == "add":
            cls.add(*argument)
            output.append(None)
        elif operation == "remove":
            cls.remove(*argument)
            output.append(None)
        elif operation == "contains":
            output.append(cls.contains(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["MyHashSet", "add", "add", "contains", "contains",
        "add", "contains", "remove", "contains"],
    ["MyHashSet", "contains", "remove", "add", "add", "contains", "remove", "contains", "contains", "add", "add", "add", "add", "remove", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "contains", "add", "contains", "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "add", "add", "contains", "add", "add", "add", "remove", "contains", "add", "contains", "add", "add", "add", "add", "add",
        "contains", "remove", "remove", "add", "remove", "contains", "add", "remove", "add", "add", "add", "add", "contains", "contains", "add", "remove", "remove", "remove", "remove", "add", "add", "contains", "add", "add", "remove", "add", "add", "add", "add", "add", "add", "add", "add", "remove", "add", "remove", "remove", "add", "remove", "add", "remove", "add", "add", "add", "remove", "remove", "remove", "add", "contains", "add"]
]

arguments_list = [
    [[], [1], [2], [1], [3], [2], [2], [2], [2]],
    [[], [72], [91], [48], [41], [96], [87], [48], [49], [84], [82], [24], [7], [56], [87], [81], [55], [19], [40], [68], [23], [80], [53], [76], [93], [95], [95], [67], [31], [80], [62], [73], [97], [33], [28], [62], [81], [57], [40], [11], [89], [28], [97], [86], [20], [5], [77], [52], [57], [88], [
        20], [48], [42], [86], [49], [62], [53], [43], [98], [32], [15], [42], [50], [19], [32], [67], [84], [60], [8], [85], [43], [59], [65], [40], [81], [55], [56], [54], [59], [78], [53], [0], [24], [7], [53], [33], [69], [86], [7], [1], [16], [58], [61], [34], [53], [84], [21], [58], [25], [45], [3]]
]

expected_output_list = [
    [None, None, None, True, False, None, True, None, False],
    [None, False, None, None, None, False, None, True, False, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, None, True, None, None, True, None, None, None, None, None, None, None, None, True, None, None, None, None, False, None, False, None, None, None, None,
        None, True, None, None, None, None, True, None, None, None, None, None, None, True, True, None, None, None, None, None, None, None, False, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, None]
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
myHashSet = MyHashSet()
myHashSet.add(1)  # set = [1]
myHashSet.add(2)  # set = [1, 2]
print(myHashSet.contains(1))  # return True
print(myHashSet.contains(3))  # return False, (not found)
myHashSet.add(2)  # set = [1, 2]
print(myHashSet.contains(2))  # return True
myHashSet.remove(2)  # set = [1]
print(myHashSet.contains(2))  # return False, (already removed)
