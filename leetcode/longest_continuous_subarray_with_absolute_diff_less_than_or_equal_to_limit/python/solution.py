class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        from collections import deque
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing queue, monotonic decreasing queue
            A: sliding window
        """

        # Store min value in monotonic increasing queue.
        # deque([(number, index), ...])
        inc = deque()
        # Store max value in monotonic decreasing queue.
        # deque([(number, index), ...])
        dec = deque()
        left = 0
        res = 0

        for right, num in enumerate(nums):
            while inc and inc[-1][0] > num:
                inc.pop()
            inc.append((num, right))

            while dec and dec[-1][0] < num:
                dec.pop()
            dec.append((num, right))

            while dec[0][0] - inc[0][0] > limit:
                if inc[0][1] == left:
                    inc.popleft()
                if dec[0][1] == left:
                    dec.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res


print(Solution().longestSubarray([8, 2, 4, 7], 4) == 2)
print(Solution().longestSubarray([1, 5, 6, 7, 8, 10, 6, 5, 6], 4) == 5)
print(Solution().longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4)
print(Solution().longestSubarray([4, 2, 2, 2, 4, 4, 2, 2], 0) == 3)
print(Solution().longestSubarray([4, 10, 2, 6, 1], 10) == 5)
print(Solution().longestSubarray([1, 8, 6, 10], 8) == 3)
