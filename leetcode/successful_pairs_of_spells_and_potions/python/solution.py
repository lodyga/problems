class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Time complexity: O(mlogm + nlogm)
            n: spell count 
            m: potion count
        Auxiliary space complexity: O(n + m)
        Tags: 
            DS: array
            A: binary search, sorting
        """
        potions.sort()
        res = []

        for spell in spells:
            left = 0
            right = len(potions) - 1
            min_right = len(potions)
            threshold = success / spell

            while left <= right:
                middle = (left + right) >> 1
                middle_num = potions[middle]

                if middle_num * spell < success:
                # if middle_num < threshold:
                    left = middle + 1
                else:
                    min_right = middle
                    right = middle - 1

            res.append(len(potions) - min_right)
            
        return res


print(Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3])
print(Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2])
print(Solution().successfulPairs([39, 34, 6, 35, 18, 24, 40], [27, 37, 33, 34, 14, 7, 23, 12, 22, 37], 43) == [10, 10, 9, 10, 10, 10, 10])
