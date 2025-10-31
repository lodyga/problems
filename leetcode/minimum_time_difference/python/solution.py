class Solution:
    def findMinDifference(self, time_points: list[str]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        cycle = 24 * 60
        minute_list = [cycle] * len(time_points)
        
        for index, time_point in enumerate(time_points):
            minutes = int(time_point[3:])
            hours = int(time_point[:2])
            minutes += hours * 60
            minute_list[index] = minutes

        minute_list.sort()
        minute_list.append(minute_list[0] + cycle)

        min_diff = cycle
        for index in range(len(minute_list) - 1):
            min_diff = min(min_diff, minute_list[index + 1] - minute_list[index])
            if min_diff == 0:
                break
        return min_diff


print(Solution().findMinDifference(["23:59", "00:00"]) == 1)
print(Solution().findMinDifference(["00:00", "23:59", "00:00"]) == 0)
print(Solution().findMinDifference(["02:39", "10:26", "21:43"]) == 296)
print(Solution().findMinDifference(["00:01", "01:59"]) == 118)