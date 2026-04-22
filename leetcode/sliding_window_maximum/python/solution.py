class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic decreasing queue, deque
            A: iteration
        """
        from collections import deque
        # deque([(number, index), ...])
        deq = deque()
        res = []

        for idx, num in enumerate(nums):
            while deq and deq[-1][0] <= num:
                deq.pop()

            deq.append((num, idx))

            while deq[0][1] <= idx - k:
                deq.popleft()

            if idx + 1 >= k:
                res.append(deq[0][0])

        return res


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: iteration
        """
        import heapq
        heap = []
        res = []

        for idx, num in enumerate(nums):
            heapq.heappush(heap, (-num, idx))

            while heap[0][1] <= idx - k:
                heapq.heappop(heap)

            if idx + 1 >= k:
                res.append(-heap[0][0])

        return res


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: brute-force
        """
        return [
            max(nums[index: index + k])
            for index in range(len(nums) - k + 1)
        ]


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7])
print(Solution().maxSlidingWindow([1], 1) == [1])
print(Solution().maxSlidingWindow([7, 2, 4], 2) == [7, 4])
print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5])
print(Solution().maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3) == [2, 2, 4, 4, 6])
