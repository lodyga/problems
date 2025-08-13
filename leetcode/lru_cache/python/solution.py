class LRUCache:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(c)
        O(capacity)
    Tags: hash map
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


class ListNode:
    def __init__(self, key=None, val=None, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(c)
        O(capacity)
    Tags: linked list
    doubly linked list
    """

    def __init__(self, capacity: int) -> None:
        self.cache = {}  # {key: node}
        self.capacity = capacity
        self.first = ListNode()
        self.last = ListNode(None, None, None, self.first)
        self.first.next = self.last

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.delete_node(node)
        self.push_node(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.delete_node(node)
        elif len(self.cache) == self.capacity:
            lru_node = self.first.next
            del self.cache[lru_node.key]
            self.delete_node(lru_node)
        
        node = ListNode(key, val)
        self.push_node(node)
        self.cache[key] = node

    
    def push_node(self, node: ListNode) -> None:
        next = self.last
        prev = next.prev
        node.next = next
        node.prev = prev
        next.prev = node
        prev.next = node
    
    def delete_node(self, node: ListNode):
        node.prev.next, node.next.prev = node.next, node.prev




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

    return output



# Example Input
# operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# expected_output = [None, None, None, 1, None, -1, None, -1, 3, 4]

operations = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
arguments = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
expected_output = [None, None, None, None, None, None, -1, None, 19, 17, None, -1, None, None, None, -1, None, -1, 5, -1, 12, None, None, 3, 5, 5, None, None, 1, None, -1, None, 30, 5, 30, None, None, None, -1, None, -1, 24, None, None, 18, None, None, None, None, -1, None, None, 18, None, None, -1, None, None, None, None, None, 18, None, None, -1, None, 4, 29, 30, None, 12, -1, None, None, None, None, 29, None, None, None, None, 17, 22, 18, None, None, None, -1, None, None, None, 20, None, None, None, -1, 18, 18, None, None, None, None, 20, None, None, None, None, None, None, None]


# Run tests
actual_output = test_input(operations, arguments)
print(actual_output == expected_output)
# print(actual_output)


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

# lRUCache2 = LRUCache(2)
# print(lRUCache2.get(2))  # return -1
# lRUCache2.put(2, 6)
# print(lRUCache2.get(1))  # return -1
# lRUCache2.put(1, 5)
# lRUCache2.put(1, 2)
# print(lRUCache2.get(1))  # return 2
# print(lRUCache2.get(2))  # return 6

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
    Auxiliary space complexity: O(n)
    Tags: hash map
    three hash maps: (cache, {key: index}, {index: key})
    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.key_to_index = {}
        self.index_to_key = {}
        self.next_index = 0
        self.lru_index = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_index:
            return -1

        index = self.key_to_index[key]
        self.index_to_key.pop(index)
        self.index_to_key[self.next_index] = key
        self.key_to_index[key] = self.next_index
        self.next_index += 1
        self.lru_index += 1
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            index = self.key_to_index[key]
            self.index_to_key.pop(index)
            self.lru_index += 1
        elif len(self.cache) == self.capacity:
            # for some data inputs return error
            # prev_key = self.index_to_key[self.lru_index]
            # self.cache.pop(prev_key)
            # self.index_to_key.pop(self.lru_index)
            # self.key_to_index.pop(prev_key)
            # self.lru_index += 1

            # prev indexes are in ascending order but are not contiguous
            prev_index = next(iter(self.index_to_key))
            prev_key = self.index_to_key[prev_index]
            self.index_to_key.pop(prev_index)
            self.cache.pop(prev_key)
            self.key_to_index.pop(prev_key)
            self.lru_index += 1

        self.key_to_index[key] = self.next_index
        self.index_to_key[self.next_index] = key
        self.cache[key] = value
        self.next_index += 1


# O(1), O(n)
# Built-In Data Structure
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the accessed key to the end to mark it as recently used
            self.cache.move_to_end(key)
            
            return self.cache[key]
        else:
            return -1

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