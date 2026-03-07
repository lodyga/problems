import heapq
from sortedcontainers import SortedSet


class SeatManager:
    """
    Time complexity: O(nlogn)
    Auxiliary space complexity: O(n)
    Tags:
        DS: heap
        A: iteration
    """

    def __init__(self, n: int):
        self.seats = []
        self.next_seat = 1

    def reserve(self) -> int:
        if self.seats:
            return heapq.heappop(self.seats)
        else:
            self.next_seat += 1
            return self.next_seat - 1

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)


class SeatManager:
    """
    Time complexity: O(nlogn)
    Auxiliary space complexity: O(n)
    Tags:
        DS: sorted set
        A: iteration
    """

    def __init__(self, n: int):
        self.seats = SortedSet()
        self.next_seat = 1

    def reserve(self) -> int:
        if self.seats:
            return self.seats.pop(0)
        else:
            self.next_seat += 1
            return self.next_seat - 1

    def unreserve(self, seatNumber: int) -> None:
        self.seats.add(seatNumber)


seatManager = SeatManager(5)
print(seatManager.reserve() == 1)
print(seatManager.reserve() == 2)
seatManager.unreserve(2)
print(seatManager.reserve() == 2)
print(seatManager.reserve() == 3)
print(seatManager.reserve() == 4)
print(seatManager.reserve() == 5)
seatManager.unreserve(5)
