class Solution:
    def maxScore(self, points: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        N = len(points)
        num_sum = sum(points)

        if N == k:
            return num_sum

        min_window = num_sum
        window = 0
        window_size = N - k
        left = 0

        for right, point in enumerate(points):
            window += point

            if right < window_size - 1:
                continue

            min_window = min(min_window, window)

            left_point = points[left]
            window -= left_point
            left += 1

        return num_sum - min_window


print(Solution().maxScore([1, 2], 2) == 3)
print(Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12)
print(Solution().maxScore([2, 2, 2], 2) == 4)
print(Solution().maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55)
