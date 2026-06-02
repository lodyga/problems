class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Time complexity: O(mlogm + nlogm)
            n: spell count 
            m: potion count
        Auxiliary space complexity: O(n + m)
        Tags:
            DS: list
            A: binary search, sorting
        """
        N = len(potions)
        potions.sort()
        res = []

        for spell in spells:
            left = 0
            right = N - 1
            fail_counter = N
            potion_threshold = success / spell

            while left <= right:
                mid = (left + right) // 2
                mid_potion = potions[mid]

                if mid_potion < potion_threshold:
                    left = mid + 1
                else:
                    fail_counter = mid
                    right = mid - 1

            res.append(N - fail_counter)

        return res


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Time complexity: O(mlogm + nlogm)
            n: spell count 
            m: potion count
        Auxiliary space complexity: O(n + m)
        Tags:
            DS: list
            A: sorting, build-in function
        """
        import bisect
        N = len(potions)
        potions.sort()
        res = []
        
        for spell in spells:
            idx = bisect.bisect_left(potions, success / spell)
            res.append(N - idx)

        return res


print(Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3])
print(Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2])
print(Solution().successfulPairs([39, 34, 6, 35, 18, 24, 40], [27, 37, 33, 34, 14, 7, 23, 12, 22, 37], 43) == [10, 10, 9, 10, 10, 10, 10])
