class MyCalendarTwo:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags: iteration
    """

    def __init__(self):
        self.events = []
        self.doubled = []

    def book(self, start: int, end: int) -> bool:
        for event_start, event_end in self.doubled:
            if (
                start < event_end and
                end > event_start
            ):
                return False

        for event_start, event_end in self.events:
            if (
                start < event_end and
                end > event_start
            ):
                doubled_start = max(start, event_start)
                doubled_end = min(end, event_end)
                self.doubled.append((doubled_start, doubled_end))

        self.events.append((start, end))
        return True


from sortedcontainers import SortedList


class MyCalendarTwo:
    """
    Time complexity: O(logn)
    Auxiliary space complexity: O(n)
    Tags: binary search
    Doesn't work
    """

    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        events = self.events
        index = events.bisect_right((start, end))

        if (
            index > 1 and
            start < events[index - 2][1]
        ):
            return False

        if (
            index < len(events) - 1 and
            end > events[index + 1][0]
        ):
            return False
        
        if (
            0 < index < len(events) and
            (
                end > max(events[index - 1][0], events[index][0]) or 
                start < min(events[index - 1][1], events[index][1])
            )
        ):
            return False

        events.add((start, end))
        return True


myCalendarTwo = MyCalendarTwo()
print(myCalendarTwo.book(10, 20))  # return True, The event can be booked. 
print(myCalendarTwo.book(50, 60))  # return True, The event can be booked. 
print(myCalendarTwo.book(10, 40))  # return True, The event can be double booked. 
print(myCalendarTwo.book(5, 15))  # return False, The event cannot be booked, because it would result in a triple booking.
print(myCalendarTwo.book(5, 10))  # return True, The event can be booked, as it does not use time 10 which is already double booked.
print(myCalendarTwo.book(25, 55))  # return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.