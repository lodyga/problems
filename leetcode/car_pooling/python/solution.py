import heapq


class Solution:
    def carPooling(self, trips: list[list[int]], cap: int) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: heap
            A: line sweep, sorting, iteration
        """
        trips.sort(key=lambda x: x[1])
        # heap((end, passengers), )
        exit_heap = []

        for passengers, start, end in trips:
            while exit_heap and exit_heap[0][0] <= start:
                _, exit_passengers = heapq.heappop(exit_heap)
                cap += exit_passengers

            cap -= passengers
            if cap < 0:
                return False

            heapq.heappush(exit_heap, (end, passengers))

        return True


class Solution:
    def carPooling(self, trips: list[list[int]], cap: int) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: line sweep, prefix sum, sorting, iteration
        """
        events = []
        for passengers, start, end in trips:
            events.append((start, passengers))
            events.append((end, -passengers))
        events.sort()

        total = 0
        for _, passengers in events:
            total += passengers
            if total > cap:
                return False
        
        return True


class Solution:
    def carPooling(self, trips: list[list[int]], cap: int) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: line sweep, iteration
        """
        UPPER_BOUND = 1001
        time_line = [0] * UPPER_BOUND

        for passengers, start, end in trips:
            time_line[start] += passengers
            time_line[end] -= passengers

        for index in range(UPPER_BOUND):
            cap -= time_line[index]
            if cap < 0:
                return False
    
        return True


print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 4) == False)
print(Solution().carPooling([[2, 1, 5], [3, 3, 7]], 5) == True)
print(Solution().carPooling([[4, 5, 6], [6, 4, 7], [4, 3, 5], [2, 3, 5]], 13) == True)
print(Solution().carPooling([[2, 1, 5], [1, 2, 3], [3, 3, 7]], 4) == False)
print(Solution().carPooling([[9, 3, 6], [8, 1, 7], [6, 6, 8], [8, 4, 9], [4, 2, 9]], 28) == False)
