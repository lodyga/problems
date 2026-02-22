class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals, sorting
        """
        meetings.sort()
        counter = 0
        prev_end = 0

        for start, end in meetings:
            counter += max(0, start - 1 - prev_end)
            prev_end = max(prev_end, end)

        return counter + (days - prev_end)


print(Solution().countDays(10, [[5, 7], [1, 3], [9, 10]]) == 2)
print(Solution().countDays(5, [[2, 4], [1, 3]]) == 1)
print(Solution().countDays(6, [[1, 6]]) == 0)
print(Solution().countDays(57, [[3, 49], [23, 44], [21, 56], [26, 55], [23, 52], [2, 9], [1, 48], [3, 31]]) == 1)
print(Solution().countDays(14, [[6, 11], [7, 13], [8, 9], [5, 8], [3, 13], [11, 13], [1, 3], [5, 10], [8, 13], [3, 9]]) == 1)
