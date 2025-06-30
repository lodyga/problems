from collections import deque


class Solution:
    def maxSlidingWindow(self, numbers: list[int], window_size: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sliding window, deque, monotonic queue
        monotonically decreasing queue
        """
        left = 0
        window = deque()  # deque((number, index), ...)
        max_list = [0] * (len(numbers) - window_size + 1)

        for right, number in enumerate(numbers):
            # Remove elements from the front of the deque if they are outside the current window.
            while window and window[0][1] < left:
                window.popleft()

            # Remove elements from the back of the deque if they are less than or equal to
            # the current number, as they cannot be the maximum in the current 
            # or any future window. monotonically decreasing queue
            while window and window[-1][0] <= number:
                window.pop()
            
            window.append((number, right))

            if right - left + 1 == window_size:
                # The max window value it a the beginning of the queue
                max_list[left] = window[0][0]
                left += 1

        return max_list


import heapq


class Solution:
    def maxSlidingWindow(self, numbers: list[int], k: int) -> list[int]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sliding window, heap
        """
        left = 0
        window = []
        heapq.heapify(window)
        max_list = [0] * (len(numbers) - k + 1)

        for right, number in enumerate(numbers):
            heapq.heappush(window, (-number, right))

            if right + 1 >= k:
                while left > window[0][1]:
                    heapq.heappop(window)

                max_list[left] = -window[0][0]
                left += 1

        return max_list


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7])
print(Solution().maxSlidingWindow([1], 1) == [1])
print(Solution().maxSlidingWindow([7, 2, 4], 2) == [7, 4])
print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3) == [3, 3, 2, 5])
print(Solution().maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], 3) == [2, 2, 4, 4, 6])


# O(n2), O(n)
# brute force
class Solution:
    def maxSlidingWindow(self, numbers: list[int], k: int) -> list[int]:
        left = 0
        sol = []

        for right in range(k - 1, len(numbers)):
            sol.append(max(numbers[left: right + 1]))

            left += 1
        return sol