class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: intervals, greedy
        """
        merged_intervals = []

        for index, (start, end) in enumerate(intervals):
            new_start = new_interval[0]
            new_end = new_interval[1]
            
            if new_end < start:
                merged_intervals.append(new_interval)
                merged_intervals.extend(intervals[index:])
                return merged_intervals  # early exit
            elif new_start > end:
                merged_intervals.append([start, end])
            else:
                new_interval = [
                    min(start, new_start), 
                    max(end, new_end)
                ]

        merged_intervals.append(new_interval)
        return merged_intervals



print(Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]])
print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]])
print(Solution().insert([], [5, 7]) == [[5, 7]])
print(Solution().insert([[1, 5]], [2, 3]) == [[1, 5]])
print(Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1]) == [[0, 1], [2, 5], [6, 7], [8, 9]])