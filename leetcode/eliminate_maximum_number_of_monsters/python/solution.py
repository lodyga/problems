class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: sorting
        """
        distance = [(d + s - 1) // s for d, s in zip(dist, speed)]
        # distance = [(d - 1) // s + 1 for d, s in zip(dist, speed)]
        distance.sort()

        for time_stamp, arrival in enumerate(distance):
            if arrival <= time_stamp:
                return time_stamp

        return len(distance)


class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        import heapq
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: sorting
        """
        distance = [(d + s - 1) // s for d, s in zip(dist, speed)]
        heapq.heapify(distance)

        for time_stamp in range(len(distance)):
            if heapq.heappop(distance) <= time_stamp:
                return time_stamp

        return len(speed)


print(Solution().eliminateMaximum([1, 3, 4], [1, 1, 1]) == 3)
print(Solution().eliminateMaximum([1, 1, 2, 3], [1, 1, 1, 1]) == 1)
print(Solution().eliminateMaximum([3, 2, 4], [5, 3, 2]) == 1)
print(Solution().eliminateMaximum([4, 3, 3, 3, 4], [1, 1, 1, 1, 4]) == 3)
print(Solution().eliminateMaximum([46, 33, 44, 42, 46, 36, 7, 36, 31, 47, 38, 42, 43, 48, 48, 25, 28, 44, 49, 47, 29, 32, 30, 6, 42, 9, 39, 48, 22, 26, 50, 34, 40, 22, 10, 45, 7, 43, 24, 18, 40, 44, 17, 39, 36], [1, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 7, 1, 1, 3, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 8, 1, 1, 1, 3, 6, 1, 3, 1, 1]) == 7)
