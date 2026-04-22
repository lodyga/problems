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
        def is_enough_time(mid: int) -> bool:
            res = 0
            for pile in piles:
                res += 1 + ((pile - 1) // mid)

                if res > hours:
                    return False
            return True

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2

            if is_enough_time(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


print(Solution().minEatingSpeed([3, 6, 7, 11], 8), 4)
print(Solution().minEatingSpeed([3, 6, 7, 11], 8) == 4)
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5) == 30)
print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 6) == 23)
print(Solution().minEatingSpeed([312884470], 312884469) == 2)
print(Solution().minEatingSpeed([3], 2) == 2)
