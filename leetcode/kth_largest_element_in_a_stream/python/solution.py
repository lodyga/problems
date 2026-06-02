import heapq


class KthLargest:
    """
    Time complexity:
        constructor: O(nlogn)
        add: O(log(k))
        n: stream size
        k: highest test scores size
    Auxiliary space complexity: O(1)
    Tags:
        DS: heap
        A: iteration
    """

    def __init__(self, k: int, stream: list[int]) -> None:
        self.k = k
        self.stream = stream
        heapq.heapify(self.stream)

        while len(self.stream) > k:
            heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        else:
            heapq.heappushpop(self.stream, val)

        return self.stream[0]


class KthLargest2:
    """
    Time complexity:
        constructor: O(nlogn)
        add: O(klog(k))
        n: stream size
        k: highest test scores size
    Auxiliary space complexity: O(n + k)
    Tags:
        DS: list
        A: sorting
    """

    def __init__(self, k: int, stream: list[int]):
        self.k = k
        self.stream = sorted(stream, reverse=True)[: self.k]

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort(reverse=True)
        
        if len(self.stream) > self.k:
            self.stream.pop()
        
        return self.stream[-1]


# Example 1
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3) == 4)
print(kthLargest.add(5) == 5)
print(kthLargest.add(10) == 5)
print(kthLargest.add(9) == 8)
print(kthLargest.add(4) == 8)
