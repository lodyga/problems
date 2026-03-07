class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """
        Time complexity: O(nlogt)
            t: upper time limit
        Auxiliary space complexity: O(n)
        Tags:
            A: binary search
        """
        # Time to reapiar all cars.
        left = 1
        right = min(ranks) * cars**2
        res = right

        while left <= right:
            mid = (left + right) // 2
            repaired_cars = sum(
                int((mid / rank)**0.5)
                for rank in ranks)

            if repaired_cars < cars:
                left = mid + 1
            else:
                res = mid
                right = mid - 1

        return res


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """
        Time complexity: O(nlogt)
            t: upper time limit
        Auxiliary space complexity: O(n)
        Tags:
            A: binary search
        """
        def are_cars_repaired(mid):
            repaired_cars = 0

            for rank in ranks:
                repaired_cars += int((mid / rank)**0.5)

                if repaired_cars >= cars:
                    return True

            return False

        # Time to reapiar all cars.
        left = 1
        right = min(ranks) * cars**2
        res = right

        while left <= right:
            mid = (left + right) // 2

            if are_cars_repaired(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


print(Solution().repairCars([4, 2, 3, 1], 10) == 16)
print(Solution().repairCars([5, 1, 8], 6) == 16)
