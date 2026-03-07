class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals, sorting
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))
        (a, b) = (-1, -1)
        res = 0

        for start, end in intervals:
            if start > b:
                res += 2
                (a, b) = (end - 1, end)
            elif start > a:
                res += 1
                (a, b) = (b, end)

        return res


print(Solution().intersectionSizeTwo([[2, 3]]) == 2)
print(Solution().intersectionSizeTwo([[1, 3], [3, 7], [8, 9]]) == 5)
print(Solution().intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]) == 3)
print(Solution().intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]) == 5)
print(Solution().intersectionSizeTwo([[1, 3], [3, 7], [5, 7], [7, 8]]) == 5)
print(Solution().intersectionSizeTwo([[2, 10], [3, 7], [3, 15], [4, 11], [6, 12], [6, 16], [7, 8], [7, 11], [7, 15], [11, 12]]) == 5)
print(Solution().intersectionSizeTwo([[1, 15], [0, 8], [13, 14]]) == 4)


class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        """
        Failed
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: intervals, sorting
        """
        if len(intervals) == 1:
            return 2

        intervals.sort()
        res = 0
        prev_end = intervals[0][1]
        fixed = prev_end if prev_end == intervals[1][0] else False

        for start, end in intervals[1:]:
            if fixed and fixed < start:
                res += 1
                fixed = False

            if min(prev_end, end) - start >= 1:
                prev_end = min(prev_end, end)
            elif prev_end == start:
                res += 1
                fixed = start
                prev_end = end
            elif prev_end < start:
                fixed = False
                res += 2
                prev_end = end

        return res + (2 if fixed else 1)
