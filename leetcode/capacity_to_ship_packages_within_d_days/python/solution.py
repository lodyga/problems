class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        left = max(weights)
        right = sum(weights)

        while left < right:
            middle_capacity = (left + right) // 2
            days_needed = 1
            current_capacity = middle_capacity

            for weight in weights:
                current_capacity -= weight

                if current_capacity < 0:
                    days_needed += 1
                    current_capacity = middle_capacity - weight

            if days_needed <= days:
                right = middle_capacity
            else:
                left = middle_capacity + 1

        return right


print(Solution().shipWithinDays([1, 2, 3, 1, 1], 4) == 3)
print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15)
print(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6)
print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == 55)
print(Solution().shipWithinDays([3, 3, 3, 3, 3, 3], 2) == 9)


class Solution:
    def days_to_ship(self, capacity: int) -> int:
        days = 1  # days to ship with current capacity
        current_capacity = capacity  # capacity for current day

        for weight in self.weights:
            if current_capacity - weight < 0:  # if ship capacity in bounds
                days += 1  # increse days to ship
                current_capacity = capacity

            current_capacity -= weight  # add a cargo to the current ship

        return days  # days to ship with current capacity

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        self.weights = weights
        low_capacity = max(weights)  # min ship cargo
        high_capacity = sum(weights)  # max ship cargo

        while low_capacity < high_capacity:
            # capacity of a cargo
            capacity = (low_capacity + high_capacity) // 2

            if (self.days_to_ship(capacity) > days):  # if more days to ship than planned
                low_capacity = capacity + 1  # increase capacity
            else:
                high_capacity = capacity  # decrease capacity

        return high_capacity