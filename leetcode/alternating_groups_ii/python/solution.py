class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        prev_color = None
        left = 0
        group_counter = 0

        for true_right in range(2 * len(colors) - 1):
            right = true_right % len(colors)
            color = colors[right]

            if prev_color == color:
                left = true_right
                if left >= len(colors):
                    break
                continue
            elif true_right - left + 1 < k:
                prev_color = color
                continue

            group_counter += 1
            prev_color = color
            if left == len(colors) - 1:
                break
            left += 1
        
        return group_counter


print(Solution().numberOfAlternatingGroups([0, 1, 0, 1, 0], 3), 3)
print(Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6), 2)
print(Solution().numberOfAlternatingGroups([1, 1, 0, 1], 4), 0)
print(Solution().numberOfAlternatingGroups([0, 1, 1], 3), 1)