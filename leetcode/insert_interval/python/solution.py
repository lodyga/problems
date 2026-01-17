class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: intervals, greedy
        """
        new_start, new_end = new_interval
        new_intervals = []

        for start, end in intervals:
            # New interval already added
            # or new interval is after current interval.
            if (
                new_interval is None or
                end < new_start
            ):
                new_intervals.append([start, end])

            # New interval is before current interval.
            elif new_end < start:
                new_intervals.append(new_interval)
                new_intervals.append([start, end])
                new_interval = None

            # New and current intervals overlaps.
            else:
                new_interval = [min(start, new_start), max(end, new_end)]
                new_start, new_end = new_interval

        if new_interval:
            new_intervals.append(new_interval)

        return new_intervals


print(Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
print(Solution().insert([], [5, 7]) == [[5, 7]])
print(Solution().insert([[1, 5]], [2, 3]) == [[1, 5]])
print(Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1]) == [[0, 1], [2, 5], [6, 7], [8, 9]])
print(Solution().insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]])
