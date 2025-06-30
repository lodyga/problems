class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: intervals, sorting
        """
        intervals.sort()
        merged_intervals = [intervals[0]]

        for index, (start, end) in enumerate(intervals[1:], 1):
            prev_end = merged_intervals[-1][1]
            if prev_end >= start:
                merged_intervals[-1][1] = max(prev_end, end)
            else:
                merged_intervals.append([start, end])
            
        return merged_intervals


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
print(Solution().merge([[1, 4], [4, 5]]) == [[1, 5]])
print(Solution().merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]])
print(Solution().merge([[1, 4], [2, 3]]) == [[1, 4]])