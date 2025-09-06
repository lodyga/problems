import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        trips.sort(key=lambda x: x[1])
        min_heap = []  # heap((end, passengers), )

        for passengers, start, end in trips:
            while min_heap and min_heap[0][0] <= start:
                _, prev_passengers = heapq.heappop(min_heap)
                capacity += prev_passengers

            heapq.heappush(min_heap, (end, passengers))
            capacity -= passengers
            if capacity < 0:
                return False

        return True


print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4) == False)
print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5) == True)
print(Solution().carPooling([[4, 5, 6], [6, 4, 7], [4, 3, 5], [2, 3, 5]], 13) == True)
print(Solution().carPooling([[2, 1, 5], [1, 2, 3], [3, 3, 7]], 4) == False)
print(Solution().carPooling([[9, 3, 6], [8, 1, 7],[6, 6, 8], [8, 4, 9], [4, 2, 9]], 28) == False)