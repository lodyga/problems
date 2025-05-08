class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyHashSet:
    """
    Time complexity:
        constructor: O(n)
        add: O(1)
        contains: O(1)
        remove: O(1)
    Auxiliary space complexity: O(n)
    Tags: linked list, hash set
    """

    def __init__(self):
        self.bucket_size = 10**4
        self.buckets = [None] * self.bucket_size

    def add(self, key: int):
        index = self.get_hash_code(key)

        if not self.buckets[index]:
            self.buckets[index] = ListNode(None, ListNode(key))
            return

        node = self.buckets[index]
        while node.next:
            if node.next.val == key:
                return
            node = node.next

        node.next = ListNode(key)

    def contains(self, key: int) -> bool:
        index = self.get_hash_code(key)
        if not self.buckets[index]:
            return False

        node = self.buckets[index].next

        while node:
            if node.val == key:
                return True
            else:
                node = node.next

        return False

    def remove(self, key: int):
        index = self.get_hash_code(key)
        if not self.buckets[index]:
            return

        node = self.buckets[index]

        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                break
            else:
                node = node.next

    def get_hash_code(self, key):
        return key % self.bucket_size


myHashSet = MyHashSet()
myHashSet.add(1)  # set = [1]
myHashSet.add(2)  # set = [1, 2]
print(myHashSet.contains(1))  # return True
print(myHashSet.contains(3))  # return False, (not found)
myHashSet.add(2)  # set = [1, 2]
print(myHashSet.contains(2))  # return True
myHashSet.remove(2)  # set = [1]
print(myHashSet.contains(2))  # return False, (already removed)