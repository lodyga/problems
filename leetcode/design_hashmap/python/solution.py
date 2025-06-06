class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    """
    Time complexity: 
        put: O(1)
        get: O(1)
        remove: O(1)
    Auxiliary space complexity: O(n)
    Tags: linked list, hash map
    """

    def __init__(self):
        self.bucket_size = 10**4
        self.buckets = [ListNode() for _ in range(self.bucket_size)]

    def put(self, key: int, val: int):
        index = self.get_hash_code(key)
        node = self.buckets[index]

        while node.next:
            if node.next.key == key:
                node.next.val = val
                return
            else:
                node = node.next

        node.next = ListNode(key, val)

    def get(self, key: int) -> int:
        index = self.get_hash_code(key)
        node = self.buckets[index].next

        while node:
            if node.key == key:
                return node.val
            else:
                node = node.next

        return -1

    def remove(self, key: int):
        index = self.get_hash_code(key)
        node = self.buckets[index]

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            else:
                node = node.next

    def get_hash_code(self, key):
        return key % self.bucket_size


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