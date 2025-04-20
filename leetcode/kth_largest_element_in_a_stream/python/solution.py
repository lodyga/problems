import heapq


class KthLargest:
    """
    Time complexity: O(m*logk)
        m: number of `add` calls
        k: the number of highest test scores
    Auxiliary space complexity: O(k)
    Tags: heap
    """

    def __init__(self, k: int, numbers: list[int]):
        self.numbers = numbers
        self.k = k
        heapq.heapify(self.numbers)
        while len(self.numbers) > self.k:
            heapq.heappop(self.numbers)

    def add(self, val: int) -> int:
        heapq.heappushpop(self.numbers, val)
        return self.numbers[0]


class KthLargest:
    """
    Time complexity: O(m*nlogn)
        m: number of `add` calls
        n: `numbers` size
    Auxiliary space complexity: O(n + m)
    Tags: sorting
    """

    def __init__(self, k: int, numbers: list[int]):
        self.k = k
        self.numbers = sorted(numbers, reverse=True)[:self.k]

    def add(self, val: int) -> int:
        self.numbers.append(val)
        self.numbers.sort(reverse=True)
        self.numbers.pop()
        return self.numbers[-1]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3) == 4)
print(kthLargest.add(5) == 5)
print(kthLargest.add(10) == 5)
print(kthLargest.add(9) == 8)
print(kthLargest.add(4) == 8)
