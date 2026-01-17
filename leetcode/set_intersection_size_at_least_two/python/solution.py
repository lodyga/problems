class Solution:
    def intersectionSizeTwo(self, intervals: list[list[int]]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: intervals, sorting
        """
        intervals.sort(key=lambda interval: interval[1])
        set_size = 0

        for index, (start, end) in enumerate(intervals):
            if index == 0:
                (a, b) = (end, end - 1)
                set_size += 2
                continue

            if not start <= a <= end:
                set_size += 1
                a = end

            if not start <= b <= end:
                set_size += 1
                if a == end:
                    b = end - 1
                else:
                    b = a
                    a = end

        return set_size


print(Solution().intersectionSizeTwo([[1, 3], [3, 7], [8, 9]]) == 5)
print(Solution().intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]) == 3)
print(Solution().intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]) == 5)
print(Solution().intersectionSizeTwo([[2, 10], [3, 7], [3, 15], [4, 11], [6, 12], [6, 16], [7, 8], [7, 11], [7, 15], [11, 12]]) == 5)
print(Solution().intersectionSizeTwo([[1, 3], [3, 7], [5, 7], [7, 8]]) == 5)
