class Solution:
    def canPlaceFlowers(self, plots: list[int], k: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy, iteration
        """
        if k == 0:
            return True

        index = 0
        while index < len(plots):
            if (
                index + 1 < len(plots) and
                plots[index + 1] == 1
            ):
                index += 1
            elif (
                (plots[index] == 0 and
                 (index == len(plots) - 1 or
                  plots[index + 1] == 0)
                 )
            ):
                k -= 1
                if k == 0:
                    return True

            index += 2

        return False


print(Solution().canPlaceFlowers([0, 0, 0], 2) == True)
print(Solution().canPlaceFlowers([0, 1, 0], 1) == False)
print(Solution().canPlaceFlowers([1, 0, 0, 0], 1) == True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1) == True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 2) == False)
print(Solution().canPlaceFlowers([0, 0, 1, 0, 1], 1) == True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False)
print(Solution().canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0) == True)
print(Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2) == True)
