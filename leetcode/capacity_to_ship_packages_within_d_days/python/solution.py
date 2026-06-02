class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        def can_ship_in_time(capacity):
            curr_capacity = 0
            curr_days = 0

            for weight in weights:
                if curr_capacity >= weight:
                    curr_capacity -= weight
                else:
                    curr_days += 1
                    curr_capacity = capacity - weight

                    if curr_days > days:
                        return False

            return True

        left = max(weights)
        right = sum(weights)
        res = right

        while left <= right:
            mid_capacity = (left + right) // 2

            if can_ship_in_time(mid_capacity):
                res = mid_capacity
                right = mid_capacity - 1
            else:
                left = mid_capacity + 1

        return res


print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15)
print(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6)
print(Solution().shipWithinDays([1, 2, 3, 1, 1], 4) == 3)
print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 55)
print(Solution().shipWithinDays([3, 3, 3, 3, 3, 3], 2) == 9)
