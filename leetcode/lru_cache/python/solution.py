class DoublyLinkedList:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(c)
        O(capacity)
    Tags: 
        DS: doubly linked list, hash map
    """

    def __init__(self, capacity: int):
        self.left = DoublyLinkedList()
        self.right = DoublyLinkedList(None, None, self.left)
        self.left.next = self.right
        self.cache = {}  # {key: Node(val, next, prev)}
        self.vals = {}  # {key: val}
        self.capacity = capacity

    def get(self, key: int) -> int:
        vals = self.vals
        if key not in vals:
            return -1

        val = vals[key]
        self._pop_node(key)
        self._push(key, val)
        return val

    def put(self, key: int, val: int) -> None:
        cache = self.cache

        if key in cache:
            self._pop_node(key)
        elif len(cache) == self.capacity:
            self._pop_lru()

        self._push(key, val)

    def _pop_lru(self) -> None:
        node = self.left.next
        key = node.val
        self._pop_node(key)

    def _pop_node(self, key: int) -> None:
        cache = self.cache
        node = cache[key]
        left = node.prev
        right = node.next
        left.next, right.prev = right, left

        self.cache.pop(key)
        self.vals.pop(key)

    def _push(self, key: int, val: int) -> None:
        right = self.right
        left = right.prev
        node = DoublyLinkedList(key, right, left)
        left.next, right.prev = node, node

        self.cache[key] = node
        self.vals[key] = val


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "LRUCache":
            cls = LRUCache(*argument)
            output.append(None)
        elif operation == "put":
            cls.put(*argument)
            output.append(None)
        elif operation == "get":
            output.append(cls.get(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
    ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
]

arguments_list = [
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
    [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
]

expected_output_list = [
    [None, None, None, 1, None, -1, None, -1, 3, 4],
    [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1, 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1, 24, None, None, 18, None, None, None, None, -1, None, None, 18, None, None, -1, None, None, None, None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, -1, None, None, None, None, 29, None, None, None, None, 17, 22, 18, None, None, None, -1, None, None, None, 20, None, None, None, -1, 18, 18, None, None, None, None, 20, None, None, None, None, None, None, None]
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
# lRUCache1 = LRUCache(2)
# lRUCache1.put(1, 1)  # cache is {1=1}
# lRUCache1.put(2, 2)  # cache is {1=1, 2=2}
# print(lRUCache1.get(1))  # return 1
# lRUCache1.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache1.get(2))  # returns -1 (not found)
# lRUCache1.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# print(lRUCache1.get(1))  # return -1 (not found)
# print(lRUCache1.get(3))  # return 3
# print(lRUCache1.get(4))  # return 4

# Example 2
# lRUCache2 = LRUCache(2)
# print(lRUCache2.get(2))  # return -1
# lRUCache2.put(2, 6)
# print(lRUCache2.get(1))  # return -1
# lRUCache2.put(1, 5)
# lRUCache2.put(1, 2)
# print(lRUCache2.get(1))  # return 2
# print(lRUCache2.get(2))  # return 6

# Example 3
# lRUCache3 = LRUCache(2)
# lRUCache3.put(2, 1)
# lRUCache3.put(1, 1)
# lRUCache3.put(2, 3)
# lRUCache3.put(4, 1)
# print(lRUCache3.get(1))  # return -1
# print(lRUCache3.get(2))  # return 3


class LRUCache:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(c)
        O(capacity)
    Tags: 
        DS: hash map
        A: build-in function
    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache.pop(key)
        self.cache[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            lru_key = next(iter(self.cache))
            del self.cache[lru_key]

        self.cache[key] = value


class LRUCache:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(c)
        O(capacity)
    Tags: 
        DS: hash map, build-in data structurn
        A: 
    """

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move the accessed key to the end to mark it as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and mark as recently used
            self.cache.move_to_end(key)
        elif self.capacity:
            # reduce capacity
            self.capacity -= 1
        else:
            # Pop the least recently used item (first item)
            self.cache.popitem(last=False)

        # Insert or update the key-value pair
        self.cache[key] = value

