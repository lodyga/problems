class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        from collections import deque
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic decreasing queue
            A: sliding window
        """
        # deque([(number, index), ...])
        window_q = deque()
        res = []

        for right, num in enumerate(nums):
            while window_q and window_q[0][1] <= right - k:
                window_q.popleft()

            while window_q and window_q[-1][0] <= num:
                window_q.pop()

            window_q.append((num, right))

            if right < k - 1:
                continue

            res.append(window_q[0][0])

        return res


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        import heapq
        """
        Time complexity: O(nlogk)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: sliding window
        """
        window_h = []
        res = []

        for right, num in enumerate(nums):
            heapq.heappush(window_h, (-num, right))

            if right < k - 1:
                continue

            while window_h[0][1] <= right - k:
                heapq.heappop(window_h)

            res.append(-window_h[0][0])

        return res


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
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
