class Solution:
    def minEatingSpeed(self, piles: list[int], hours: int) -> int:
        """
        Time complexity: O(nlogm)
            n: pile length 
            m: highest pile stack
        Auxiliary space complexity: O(1)
        Tags: 
            A: binary search
        """
        # bnananas per hour
        left = 1
        right = max(piles)
        min_time = right

        while left <= right:
            middle = (left + right) >> 1
            hours_for_eat = 0

            for pile in piles:
                hours_for_eat += ((pile - 1) // middle) + 1
                if hours_for_eat > hours:
                    break

            if hours_for_eat > hours:
                left = middle + 1
            else:
                min_time = middle
                right = middle - 1

        return min_time


print(Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4)
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30)
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23)
print(Solution().minEatingSpeed([312884470], 312884469) == 2)
print(Solution().minEatingSpeed([3], 2) == 2)
