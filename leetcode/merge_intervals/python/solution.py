class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: intervals, greedy, sorting
        """
        intervals.sort()
        merged = [intervals[0]]

        for index in range(1, len(intervals)):
            start, end = intervals[index]

            _, prev_end = merged[-1]
            if prev_end >= start:
                merged[-1][1] = max(prev_end, end)
            else:
                merged.append([start, end])

        return merged


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
print(Solution().merge([[1, 4], [4, 5]]) == [[1, 5]])
print(Solution().merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]])
print(Solution().merge([[1, 4], [2, 3]]) == [[1, 4]])
