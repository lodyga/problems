class Solution:
    def carFleet(self, target: int, positions: list[int], speeds: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting
        """
        prev_time = 0
        fleet_counter = 0

        for position, speed in sorted(zip(positions, speeds), reverse=True):
            distance = target - position
            time = distance / speed

            if time > prev_time:
                fleet_counter += 1
                prev_time = time

        return fleet_counter


print(Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3)
print(Solution().carFleet(10, [3], [3]) == 1)
print(Solution().carFleet(100, [0, 2, 4], [4, 2, 1]) == 1)
print(Solution().carFleet(10, [0, 4, 2], [2, 1, 3]) == 1)
