from collections import defaultdict


class DoublyListNode:
    def __init__(self, value=None, next=None, prev=None) -> None:
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self) -> None:
        self.first = DoublyListNode()
        self.last = DoublyListNode(None, None, self.first)
        self.first.next = self.last
        self.len = 0

    def push(self, node) -> None:
        last = self.last
        prev_last = last.prev
        node.prev, node.next = prev_last, last
        prev_last.next, last.prev = node, node
        self.len += 1

    def pop(self) -> None:
        node = self.last.prev
        self.delete(node)

    def pop_left(self) -> None:
        node = self.first.next
        self.delete(node)
    
    def delete(self, node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        del node
        self.len -= 1
    
    def peak(self) -> int | None:
        return self.first.next.value if self.len > 0 else None
    

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_value = defaultdict(int)  # {key: value, }
        self.key_frequency = defaultdict(int)  # {key: frequency, }
        self.key_node = defaultdict(DoublyListNode)  # {key: DoublyListNode(), }
        self.frequency_bucket = defaultdict(DoublyLinkedList)  # {frequency: DoublyLinkedList(DoublyListNode(), ), }
        self.min_frequency = 0

    def _update_frequency(self, key) -> None:
        frequency = self.key_frequency[key]
        node = self.key_node[key]
        bucket = self.frequency_bucket[frequency]
        bucket.delete(node)
        if (
            frequency == self.min_frequency and 
            bucket.len == 0
        ):
            self.min_frequency += 1
        self.key_frequency[key] += 1
        frequency += 1
        self.frequency_bucket[frequency].push(node)

    def get(self, key: int) -> int:
        if key not in self.key_value:
            return -1
        self._update_frequency(key)
        return self.key_value[key]
        

    def put(self, key: int, value: int) -> None:
        # Update existing key
        if key in self.key_value:
            self.key_value[key] = value
            self._update_frequency(key)
            return
        
        # Capacity reached, pop LFU key
        if len(self.key_value) == self.capacity:
            lfu_bucket = self.frequency_bucket[self.min_frequency]
            lfu_key = lfu_bucket.peak()
            del self.key_value[lfu_key]
            del self.key_frequency[lfu_key]
            del self.key_node[lfu_key]
            lfu_bucket.pop_left()

            if lfu_bucket.len == 0:
                del self.frequency_bucket[self.min_frequency] 

        # Put new key
        self.key_value[key] = value
        self.key_frequency[key] = 1
        self.key_node[key] = DoublyListNode(key)
        self.frequency_bucket[1].push(self.key_node[key])
        self.min_frequency = 1


class LFUCache2:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags: hash map
    """

    def __init__(self, capacity: int):
        self.cache = {}  # {key: value}
        self.key_frequency = {}  # {key: frequency}
        self.frequency_bucket = {1: []}  # {frequency: [key1, key2, ...]}
        self.capacityacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        val = self.cache[key]
        self._update_frequency(key)
        return val

    def put(self, key: int, val: int) -> None:
        if (
            len(self.cache) == self.capacityacity and
            key not in self.cache
        ):
            frequency = 1  # min frequency
            while (
                frequency not in self.frequency_bucket or
                len(self.frequency_bucket[frequency]) == 0
            ):
                frequency += 1
                continue
            key_to_pop = self.frequency_bucket[frequency][0]
            self.frequency_bucket[frequency].pop(0)
            del self.cache[key_to_pop]
            del self.key_frequency[key_to_pop]

        self.cache[key] = val
        self._update_frequency(key)

    def _update_frequency(self, key: int):
        if key not in self.key_frequency:
            self.key_frequency[key] = 1
            self.frequency_bucket[1].append(key)
            return

        frequency = self.key_frequency[key]
        self.key_frequency[key] += 1
        self.frequency_bucket[frequency].remove(key)
        if frequency + 1 not in self.frequency_bucket:
            self.frequency_bucket[frequency + 1] = []
        self.frequency_bucket[frequency + 1].append(key)


lfu = LFUCache(2)
lfu.put(1, 1)  # cache=[1,_], cnt(1)=1
lfu.put(2, 2)  # cache=[2,1], cnt(2)=1, cnt(1)=1
print(lfu.get(1))
# return 1
# cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3)
# 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
# cache=[3,1], cnt(3)=1, cnt(1)=2
print(lfu.get(2))  # return -1 (not found)
print(lfu.get(3))
# return 3
# cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)
# Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
# cache=[4,3], cnt(4)=1, cnt(3)=2
print(lfu.get(1))  # return -1 (not found)
print(lfu.get(3))
# return 3
# cache=[3,4], cnt(4)=1, cnt(3)=3
print(lfu.get(4))
# return 4
# cache=[4,3], cnt(4)=2, cnt(3)=3


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "LFUCache":
            cls = LFUCache(*argument)
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
    ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
    ["LFUCache", "put", "put", "put", "put", "get"],
    ["LFUCache", "get", "put", "get", "put", "put", "get", "get"]
]

arguments_list = [
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
    [[2], [3, 1], [2, 1], [2, 2], [4, 4], [2]],
    [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]

]

expected_output_list = [
    [None, None, None, 1, None, -1, 3, None, -1, 3, 4],
    [None, None, None, None, None, 2],
    [None, -1, None, -1, None, None, 2, 6]
]


# Run tests
def run_tests(
        operations_list: list[list[str]],
        arguments_list: list[list[list[int]]],
        expected_output_list: list[list[int | None]],
        show_output: bool = False
) -> list[bool]:
    """
    Run a batch of LFUCache tests and compare outputs with expected results.
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