import heapq


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        """
        Time complexity: O(m*n*logn)
            n: nums length
            m: avg string num length
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        nums.sort(key=lambda x: (len(x), x), reverse=True)
        return nums[k - 1]


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        """
        Time complexity: O(n * m + klogn)
            n: nums length
            m: avg string num length
        Auxiliary space complexity: O(k)
        Tags: heap
        """
        max_heap = [-int(num) for num in nums]
        heapq.heapify(max_heap)
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        return str(-max_heap[0])


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        """
        Time complexity: O(m * nlogn)
            n: nums length
            m: avg string num length
        Auxiliary space complexity: O(k)
        Tags: heap
        """
        min_heap = []
        for index, num in enumerate(nums):
            if index < k:
                heapq.heappush(min_heap, int(num))
            else:
                heapq.heappushpop(min_heap, int(num))
        return str(min_heap[0])


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        """
        Time complexity: O(m * nlogn)
            n: nums length
            m: avg string num length
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        numbers = [int(num) for num in nums]
        return str(heapq.nlargest(k, numbers)[k - 1])


class LexNum:
    def __init__(self, char) -> None:
        self.char = char

    def __lt__(self, other) -> bool:
        if len(self.char) == len(other.char):
            return self.char < other.char
        else:
            return len(self.char) < len(other.char)


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        """
        Time complexity: O(m * nlogk)
            n: nums length
            m: avg string num length
        Auxiliary space complexity: O(k)
        Tags: heap
        """
        min_heap = []
        for index, num in enumerate(nums):
            if index < k:
                heapq.heappush(min_heap, LexNum(num))
            else:
                heapq.heappushpop(min_heap, LexNum(num))
        return min_heap[0].char


print(Solution().kthLargestNumber(["3", "6", "7", "10"], 4) == "3")
print(Solution().kthLargestNumber(["2", "21", "12", "1"], 3) == "2")
print(Solution().kthLargestNumber(["0", "0"], 2) == "0")
