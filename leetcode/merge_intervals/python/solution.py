class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: intervals, greedy, sorting
        """
        N = len(intervals)
        intervals.sort()
        res = [intervals[0]]

        for idx in range(1, N):
            end = res[-1][-1]
            next_start, next_end = intervals[idx]

            if end < next_start:
                res.append([next_start, next_end])
            else:
                res[-1][1] = max(end, next_end)

        return res


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
print(Solution().merge([[1, 4], [4, 5]]) == [[1, 5]])
print(Solution().merge([[4, 7], [1, 4]]) == [[1, 7]])
print(Solution().merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]])
print(Solution().merge([[1, 4], [2, 3]]) == [[1, 4]])

