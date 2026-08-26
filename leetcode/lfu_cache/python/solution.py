class DoublyLinkedNode:
    def __init__(self, key: int = -1, val: int = -1, next=None, prev=None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self, nodes: list[DoublyLinkedNode] = None) -> None:
        self.size = 0
        self.first = DoublyLinkedNode()
        self.last = DoublyLinkedNode(-1, -1, None, self.first)
        self.first.next = self.last

        if nodes:
            for node in nodes:
                self.push(node)

    def push(self, node: DoublyLinkedNode) -> None:
        right = self.last
        left = right.prev

        left.next = node
        right.prev = node

        node.next = right
        node.prev = left

        self.size += 1

    def pop(self) -> None:
        if self.size == 0:
            return

        node = self.last.prev
        self.delete(node)

    def pop_left(self) -> None:
        if self.size == 0:
            return

        node = self.first.next
        self.delete(node)

    def delete(self, node: DoublyLinkedNode) -> None:
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1

    def front(self) -> DoublyLinkedNode:
        return self.first.next if self.size > 0 else None


class LFUCache:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(c)
        O(capacity)
    Tags:
        DS: doubly linked list, hash map
    """

    def __init__(self, cap: int):
        # from collections import defaultdict
        self.cap = cap
        self.size = 0
        self.min_freq = 0

        self.nodes = {}  # {key: DoblyListNode(key, val, next, prev), }
        # self.nodes = defaultdict(DoublyLinkedNode)

        self.freqs = {}  # {key: frequency, }
        # self.freqs = defaultdict(int)

        self.freq_buckets = {}
        # {frequency: DoublyLinkedList(DoblyListNode(), ), }
        # self.freq_buckets = defaultdict(DoublyLinkedList)


    def _update_bucket(self, node: DoublyLinkedNode, freq: int) -> None:
        if freq not in self.freq_buckets:
            self.freq_buckets[freq] = DoublyLinkedList([node])
        else:
            self.freq_buckets[freq].push(node)

    def _insert(self, key: int, val: int) -> None:
        node = DoublyLinkedNode(key, val)
        self.nodes[key] = node
        self.freqs[key] = 1

        self._update_bucket(node, 1)
        self.min_freq = 1

    def _update(self, key: int, val: int) -> None:
        freq = self.freqs[key]
        node = self.nodes[key]
        node.val = val
        bucket = self.freq_buckets[freq]
        bucket.delete(node)

        if (
            freq == self.min_freq
            and bucket.size == 0
        ):
            self.min_freq += 1

        self.freqs[key] += 1
        self._update_bucket(node, self.freqs[key])

    def _pop_lru(self) -> None:
        lfu_bucket = self.freq_buckets[self.min_freq]
        lfu_key = lfu_bucket.front().key
        self.nodes.pop(lfu_key)
        self.freqs.pop(lfu_key)
        lfu_bucket.pop_left()

        if lfu_bucket.size == 0:
            self.freq_buckets.pop(self.min_freq)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        val = self.nodes[key].val
        self._update(key, val)

        return val

    def put(self, key: int, val: int) -> None:
        # Update existing key.
        if key in self.nodes:
            self._update(key, val)

        # Capacity reached -> pop LFU key.
        elif self.size == self.cap:
            self._pop_lru()
            self._insert(key, val)

        # Insert a new key.
        else:
            self._insert(key, val)
            self.size += 1


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
