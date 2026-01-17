import heapq


class KthLargest:
    """
    Time complexity: O(n*logk)
        n: number of `add` calls
        k: the number of highest test scores
    Auxiliary space complexity: O(1)
    Tags:
        DS: heap
        A: heap, in-place method
    """

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        nums = self.nums

        if len(nums) < self.k:
            heapq.heappush(nums, val)
        else:
            heapq.heappushpop(nums, val)
        return nums[0]


class KthLargest:
    """
    Time complexity: O(n*mlogm)
        n: number of `add` calls
        m: `numbers` size
    Auxiliary space complexity: O(n + m)
    Tags:
        DS: list
        A: sorting
    """

    def __init__(self, k: int, numbers: list[int]):
        self.k = k
        self.numbers = sorted(numbers, reverse=True)[:self.k]

    def add(self, val: int) -> int:
        self.numbers.append(val)
        self.numbers.sort(reverse=True)
        self.numbers.pop()
        return self.numbers[-1]



# Example 1
kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3) == 4)
print(kthLargest.add(5) == 5)
print(kthLargest.add(10) == 5)
print(kthLargest.add(9) == 8)
print(kthLargest.add(4) == 8)