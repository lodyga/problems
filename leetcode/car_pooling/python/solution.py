import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: heap
        """
        trips.sort(key=lambda x: x[1])
        passanger_heap = []  # heap((end, passengers), )

        for passengers, start, end in trips:
            while passanger_heap and passanger_heap[0][0] <= start:
                _, prev_passengers = heapq.heappop(passanger_heap)
                capacity += prev_passengers

            heapq.heappush(passanger_heap, (end, passengers))
            capacity -= passengers
            if capacity < 0:
                return False

        return True


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: iteration, brute-force
        """
        time_line = [0] * 1001

        for passengers, start, end in trips:
            time_line[start] += passengers
            time_line[end] -= passengers

        for index in range(1001):
            capacity -= time_line[index]
            if capacity < 0:
                return False
    
        return True


print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4) == False)
print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5) == True)
print(Solution().carPooling([[4, 5, 6], [6, 4, 7], [4, 3, 5], [2, 3, 5]], 13) == True)
print(Solution().carPooling([[2, 1, 5], [1, 2, 3], [3, 3, 7]], 4) == False)
print(Solution().carPooling([[9, 3, 6], [8, 1, 7],[6, 6, 8], [8, 4, 9], [4, 2, 9]], 28) == False)