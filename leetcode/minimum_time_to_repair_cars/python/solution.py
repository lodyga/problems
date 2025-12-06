class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        """
        Time complexity: O(nlogn)
            n: upper time
        Auxiliary space complexity: O(n)
        Tags: binary search
        """
        def are_cars_repaired(time):
            """
            Calculuate is it enougth `time` to reapir all cars.
            """
            total = 0
            for rank in ranks:
                total += int((time / rank)**0.5)
                # early break
                if total >= cars:
                    return True
            return False

        # time to repair some cars
        lower_time = 1
        upper_time = ranks[0] * cars**2
        min_time = upper_time

        while lower_time <= upper_time:
            middle_time = (lower_time + upper_time) // 2

            if are_cars_repaired(middle_time):
                min_time = middle_time
                upper_time = middle_time - 1
            else:
                lower_time = middle_time + 1

        return min_time


print(Solution().repairCars([4, 2, 3, 1], 10) == 16)
print(Solution().repairCars([5, 1, 8], 6) == 16)
