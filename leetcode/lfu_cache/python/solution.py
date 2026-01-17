from collections import defaultdict


class DoublyLinkedNode:
    def __init__(self, val=None, next=None, prev=None) -> None:
        # Val tores a key.
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, nodes: list[DoublyLinkedNode]) -> None:
        self.left = DoublyLinkedNode()
        self.right = DoublyLinkedNode(None, None, self.left)
        self.left.next = self.right
        self.len = 0
        if nodes:
            for node in nodes:
                self.push(node)

    def push(self, node: DoublyLinkedNode) -> None:
        right = self.right
        left = right.prev

        node.next = right
        node.prev = left

        left.next = right.prev = node
        self.len += 1

    def pop(self) -> None:
        node = self.right.prev
        self.delete(node)

    def pop_left(self) -> None:
        node = self.left.next
        self.delete(node)

    def delete(self, node: DoublyLinkedNode) -> None:
        node.next.prev, node.prev.next = node.prev, node.next
        del node
        self.len -= 1

    def peak(self) -> DoublyLinkedNode:
        # The val is actualy a key.
        # The vals are in self.vals.
        return self.left.next if self.len > 0 else None


class LFUCache:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(c)
        O(capacity)
    Tags:
        DS: doubly linked list, hash map
    """

    def __init__(self, cap: int):
        self.cap = cap
        self.nodes = {}  # {key: Node(val, next, prev)}
        # self.nodes = defaultdict(DoublyLinkedNode)  # {key: DoblyListNode()}

        self.vals = {}  # {key: val}
        # self.vals = defaultdict(int)  # {key: val}

        self.freqs = {}  # {key: frequency}
        # self.freqs = defaultdict(int)  # {key: frequency}

        # {frequency: DoublyLinkedList(DoblyListNode(), ), }
        self.freq_buckets = {}
        # self.freq_buckets = defaultdict(DoublyLinkedList)  # {frequency: DoublyLinkedList(), }
        self.min_freq = 0

    def _insert(self, key, val):
        self.vals[key] = val
        self.freqs[key] = 1
        node = DoublyLinkedNode(key)
        self.nodes[key] = node
        if 1 not in self.freq_buckets:
            self.freq_buckets[1] = DoublyLinkedList([node])
        else:
            self.freq_buckets[1].push(node)
        self.min_freq = 1

    def _update(self, key, val):
        self.vals[key] = val
        freq = self.freqs[key]
        node = self.nodes[key]
        bucket = self.freq_buckets[freq]
        bucket.delete(node)
        if (
            freq == self.min_freq and
            bucket.len == 0
        ):
            self.min_freq += 1
        self.freqs[key] += 1
        if freq + 1 not in self.freq_buckets:
            self.freq_buckets[freq + 1] = DoublyLinkedList([node])
        else:
            self.freq_buckets[freq + 1].push(node)

    def _pop_lru(self):
        lfu_bucket = self.freq_buckets[self.min_freq]
        lfu_key = lfu_bucket.peak().val
        self.vals.pop(lfu_key)
        self.nodes.pop(lfu_key)
        self.freqs.pop(lfu_key)
        lfu_bucket.pop_left()

        if lfu_bucket.len == 0:
            self.freq_buckets.pop(self.min_freq)

    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        self._update(key, self.vals[key])
        return self.vals[key]

    def put(self, key: int, val: int) -> None:
        # Update existing key.
        if key in self.nodes:
            self._update(key, val)

        # Capacity reached -> pop LFU key.
        elif self.cap == 0:
            self._pop_lru()
            self._insert(key, val)

        # Insert a new key.
        else:
            self._insert(key, val)
            self.cap -= 1


lfu = LFUCache(2)
lfu.put(1, 1)  # cache=[1,_], cnt(1)=1
lfu.put(2, 2)  # cache=[2,1], cnt(2)=1, cnt(1)=1
print(lfu.get(1) == 1)
# return 1
# cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3)
# 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
# cache=[3,1], cnt(3)=1, cnt(1)=2
print(lfu.get(2) == -1)
print(lfu.get(3) == 3)
# cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4)
# Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
# cache=[4,3], cnt(4)=1, cnt(3)=2
print(lfu.get(1) == - 1)
print(lfu.get(3) == 3)
# cache=[3,4], cnt(4)=1, cnt(3)=3
print(lfu.get(4) == 4)
# cache=[4,3], cnt(4)=2, cnt(3)=3
