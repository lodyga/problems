class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        N = len(colors)
        prev_color = -1
        left = 0
        counter = 0

        # Right exclude the last element in the second loop
        # to avoid duplicate group ending in the last element of colors.
        for right in range(2*N - 1):
            color = colors[right % N]

            if color == prev_color:
                left = right
                # If left start the second loop then break.
                if left >= N:
                    break
                continue

            prev_color = color

            # If group lenght is to short.
            if right - left + 1 < k:
                continue
            
            # If left start the second loop then break.
            if left == N:
                break
            left += 1

            counter += 1

        return counter


print(Solution().numberOfAlternatingGroups([0, 1, 0, 1, 0], 3) == 3)
print(Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6) == 2)
print(Solution().numberOfAlternatingGroups([1, 1, 0, 1], 4) == 0)
print(Solution().numberOfAlternatingGroups([0, 1, 1], 3) == 1)
print(Solution().numberOfAlternatingGroups([0, 1, 0, 1], 3) == 4)
print(Solution().numberOfAlternatingGroups([0, 0, 1, 0, 0], 3) == 1)
print(Solution().numberOfAlternatingGroups([0, 0, 1, 0, 1], 3) == 3)
