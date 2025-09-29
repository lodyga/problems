from collections import deque


class Solution:
    def longestSubarray(self, numbers: list[int], limit: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: queue, sliding window
        monotonic increasing queue, monotonic decreasing queue
        """
        # store min value; monotonic increasing queue
        inc_queue = deque()
        # store max value; monotonic decreasing queue
        dec_queue = deque()
        max_subarray_length = 1
        left = 0

        for right, number in enumerate(numbers):
            while inc_queue and inc_queue[-1][1] > number:
                inc_queue.pop()
            inc_queue.append((right, number))
            while dec_queue and dec_queue[-1][1] < number:
                dec_queue.pop()
            dec_queue.append((right, number))

            while dec_queue[0][1] - inc_queue[0][1] > limit:
                if inc_queue[0][0] == left:
                    inc_queue.popleft()
                if dec_queue[0][0] == left:
                    dec_queue.popleft()
                left += 1

            max_subarray_length = max(max_subarray_length, right - left + 1)

        return max_subarray_length


print(Solution().longestSubarray([1, 5, 6, 7, 8, 10, 6, 5, 6], 4) == 5)
print(Solution().longestSubarray([8, 2, 4, 7], 4) == 2)
print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4)
print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3)
print(Solution().longestSubarray([4, 10, 2, 6, 1], 10) == 5)