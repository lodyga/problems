class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: intervals, sorting
        """
        intervals.sort()
        clean_counter = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if prev_end > start:
                prev_end = min(prev_end, end)
                clean_counter += 1
            else:
                prev_end = end

        return clean_counter


print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1)
print(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2)
print(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0)
print(Solution().eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2)
print(Solution().eraseOverlapIntervals([[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2], [30, 47], [-40, -26]]) == 7)