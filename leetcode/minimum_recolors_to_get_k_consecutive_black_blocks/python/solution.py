class Solution:
    def minimumRecolors(self, blocks: str, window_length: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        window = 0
        max_window = 0
        for index in range(window_length):
            block = blocks[index]
            if block == "B":
                window += 1
                max_window += 1
        
        for right in range(window_length, len(blocks)):
            left = right - window_length
            window -= 1 if blocks[left] == "B" else 0
            window += 1 if blocks[right] == "B" else 0
            max_window = max(max_window, window)
            if max_window == window_length:
                return 0
        
        return window_length - max_window


print(Solution().minimumRecolors("WBBWWBBWBW", 7) == 3)
print(Solution().minimumRecolors("WBWBBBW", 2) == 0)