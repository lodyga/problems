class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        window = 0
        min_window = k
        left = 0

        for right, block in enumerate(blocks):
            if block == "W":
                window += 1

            if right < k - 1:
                continue

            min_window = min(min_window, window)
            if min_window == 0:
                break

            if blocks[left] == "W":
                window -= 1
            left += 1

        return min_window


print(Solution().minimumRecolors("WBBWWBBWBW", 7) == 3)
print(Solution().minimumRecolors("WBWBBBW", 2) == 0)
