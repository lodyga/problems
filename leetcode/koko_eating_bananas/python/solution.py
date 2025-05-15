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

        while left < right:
            middle = (left + right) // 2
            time_to_eat = sum((pile - 1) // middle + 1 for pile in piles)

            if time_to_eat <= hours:
                right = middle
            else:
                left = middle + 1
            
        return right


print(Solution().minEatingSpeed([3, 6, 7, 11], 8), 4)
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5), 30)
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6), 23)
print(Solution().minEatingSpeed([312884470], 312884469), 2)
print(Solution().minEatingSpeed([3], 2), 2)