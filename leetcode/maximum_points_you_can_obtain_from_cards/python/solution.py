class Solution:
    def maxScore(self, card_points: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        window_length = len(card_points) - k
        window = 0
        total = sum(card_points)
        min_window = total
        left = 0
        
        if window_length == 0:
            return total

        for right, card_point in enumerate(card_points):
            window += card_point

            if right - left + 1 < window_length:
                continue

            min_window = min(min_window, window)
            window -= card_points[left]
            left += 1

        return total - min_window


print(Solution().maxScore([1, 2], 2) == 3)
print(Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3) == 12)
print(Solution().maxScore([2, 2, 2], 2) == 4)
print(Solution().maxScore([9, 7, 7, 9, 7, 7, 9], 7) == 55)