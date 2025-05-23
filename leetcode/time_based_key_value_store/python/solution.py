class TimeMap:
    """
    Time complexity: 
       set(): O(1)
       get(): O(logn)
       n: max `values assigned to a key` count
    Auxiliary space complexity: O(n*m)
        m: key count
    Tags: binary search
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if (not key in self.store or
                timestamp < self.store[key][0][0]):
            return ""

        store_values = self.store[key]
        if (timestamp > store_values[-1][0]):
            return store_values[-1][1]

        left = 0
        right = len(store_values) - 1

        while left <= right:
            middle = (left + right) // 2
            middle_stamp = store_values[middle][0]

            if timestamp == middle_stamp:
                return store_values[middle][1]
            elif timestamp < middle_stamp:
                right = middle - 1
            else:
                left = middle + 1

        return store_values[right][1]


class ListNode:
    def __init__(self, val=(None, None), next=None) -> None:
        self.val = val  # (timestamp, value)
        self.next = next


class TimeMap:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
        n: max `values assigned to a key` count
    Auxiliary space complexity: O(n*m)
        m: key count
    Tags: linked list
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = ListNode()

        node = self.store[key]

        while node.next and timestamp < node.next.val[0]:
            node = node.next

        node.next = ListNode((timestamp, value), node.next)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""

        node = self.store[key]

        while node.next and timestamp < node.next.val[0]:
            node = node.next

        return node.next.val[1] if node.next else ""


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