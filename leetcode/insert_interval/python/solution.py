class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: intervals, greedy
        """
        n_start, n_end = new_interval
        res = []

        for idx, (start, end) in enumerate(intervals):
            # New interval is earlier than current interval without overlap.
            if n_end < start:
                res.append([n_start, n_end])
                res.extend(intervals[idx:])
                return res
            # New interval overlap current interterval.
            elif (
                n_start <= end and n_end >= start
                or n_end >= start and n_start <= end
            ):
                n_start = min(n_start, start)
                n_end = max(n_end, end)
            # New interval is later than current interval without overlap.
            else:
                res.append([start, end])

        res.append([n_start, n_end])
        return res


class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: intervals, greedy
        """
        n_start, n_end = new_interval
        res = []

        for idx, (start, end) in enumerate(intervals):
            # New interval is earlier than current interval without overlap.
            if n_end < start:
                res.append([n_start, n_end])
                res.extend(intervals[idx:])
                return res
            # New interval is later than current interval without overlap.
            elif n_start > end:
                res.append([start, end])
            # New interval overlap current interterval.
            else:
                n_start = min(n_start, start)
                n_end = max(n_end, end)

        res.append([n_start, n_end])
        return res


print(Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
print(Solution().insert([], [5, 7]) == [[5, 7]])
print(Solution().insert([[1, 5]], [2, 3]) == [[1, 5]])
print(Solution().insert([[2, 5], [6, 7], [8, 9]],[0, 1]) == [[0, 1], [2, 5], [6, 7], [8, 9]])
print(Solution().insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]])
