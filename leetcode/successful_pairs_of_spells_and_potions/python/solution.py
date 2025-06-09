class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Time complexity: O(mlogm + nlogm)
        Auxiliary space complexity: O(m)
        Tags: binary search
        """
        potions.sort()
        successful_spells = [0] * len(spells)

        for index, spell in enumerate(spells):
            left = 0
            right = len(potions) - 1

            while left <= right:
                middle = (left + right) // 2
                middle_potion = potions[middle]

                if middle_potion * spell >= success:
                    right = middle - 1
                else:
                    left = middle + 1
                
            successful_spells[index] = len(potions) - left
        
        return successful_spells


print(Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3])
print(Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2])
print(Solution().successfulPairs([39, 34, 6, 35, 18, 24, 40], [27, 37, 33, 34, 14, 7, 23, 12, 22, 37], 43) == [10, 10, 9, 10, 10, 10, 10])