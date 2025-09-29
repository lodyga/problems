class Solution:
    def minEatingSpeed(self, piles: list[int], hours: int) -> int:
        """
        Time complexity: O(nlogm)
            n: pile length 
            m: highest pile stack
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = 1
        right = max(piles)
        min_banana_per_hour = right

        while left <= right:
            # bananas per hour
            middle = (left + right) // 2

            time_to_eat = 0
            for pile in piles:
                time_to_eat += ((pile - 1) // middle) + 1
                if time_to_eat > hours:
                    break

            if time_to_eat <= hours:
                min_banana_per_hour = middle
                right = middle - 1
            else:
                left = middle + 1

        return min_banana_per_hour


print(Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4)
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30)
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23)
print(Solution().minEatingSpeed([312884470], 312884469) == 2)
print(Solution().minEatingSpeed([3], 2) == 2)