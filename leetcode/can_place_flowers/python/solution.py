class Solution:
    def canPlaceFlowers(self, plots: list[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        if k == 0:
            return True

        idx = 0
        while idx < len(plots):
            # Plot is planted.
            if plots[idx] == 1:
                idx += 2
            # Next plot is planted: move 3 plots.
            elif (
                idx + 1 < len(plots) and
                plots[idx + 1] == 1
            ):
                idx += 3
            # Current plot is empty and
            # it is the last plot or the next plot is empty:
            # Plant and move 2 plots.
            elif (
                (plots[idx] == 0 and
                 (idx == len(plots) - 1 or
                  plots[idx + 1] == 0)
                 )
            ):
                k -= 1
                if k == 0:
                    return True
                idx += 2

        return False


class Solution:
    def canPlaceFlowers(self, plots: list[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        N = len(plots)
        idx = 0
        placed = 0

        while idx < N:
            if idx == 0 and plots[0] == 0 and plots[1] == 0:
                placed += 1
                idx += 2
            elif idx == N - 1 and plots[N - 1] == 0 and plots[N - 2] == 0:
                placed += 1
                idx += 2
            elif 0 < idx < N - 1 and plots[idx - 1] == 0 and plots[idx] == 0 and plots[idx + 1]:
                placed += 1
                idx += 2
            else:
                idx += 1

        return placed == k


print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1) == True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2) == False)
print(Solution().canPlaceFlowers([0, 0, 0], 2) == True)
print(Solution().canPlaceFlowers([0, 1, 0], 1) == False)
print(Solution().canPlaceFlowers([1, 0, 0, 0], 1) == True)
print(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1) == True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False)
print(Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0) == True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2) == True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2) == True)
print(Solution().canPlaceFlowers([0, 1, 0, 1, 0, 1, 0, 0], 1) == True)
