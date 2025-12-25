class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags: 
            A: binary search
        """
        def can_transport(capacity):
            capacity_copy = capacity
            trans_days = 1

            for weight in weights:
                if trans_days > days:
                    return False

                capacity -= weight

                if capacity < 0:
                    trans_days += 1
                    capacity = capacity_copy - weight

            return trans_days <= days

        # capacities
        left = max(weights)
        right = sum(weights)
        res = len(weights)

        while left <= right:
            mid = (left + right) >> 1

            if can_transport(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


print(Solution().shipWithinDays([1, 2, 3, 1, 1], 4) == 3)
print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15)
print(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6)
print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 55)
print(Solution().shipWithinDays([3, 3, 3, 3, 3, 3], 2) == 9)
