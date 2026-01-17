from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic decreasing queue
            A: sliding window
        """
        window = deque()  # deque((index, num), ...)
        max_window_list = []

        for index, num in enumerate(nums):
            while window and window[0][0] < index - k + 1:
                window.popleft()

            while window and window[-1][1] <= num:
                window.pop()

            window.append((index, num))

            if index >= k - 1:
                max_window_list.append(window[0][1])

        return max_window_list


import heapq


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: sliding window
        """
        left = 0
        window = []
        max_window_list = [0] * (len(nums) - k + 1)

        for right, num in enumerate(nums):
            heapq.heappush(window, (-num, right))

            if right + 1 >= k:
                while left > window[0][1]:
                    heapq.heappop(window)

                max_window_list[left] = -window[0][0]
                left += 1

        return max_window_list


class Solution2:
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
