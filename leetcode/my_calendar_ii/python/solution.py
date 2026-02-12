class MyCalendarTwo:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: list
        A: interval, iteration
    """

    def __init__(self):
        # [(event start, event end), ]
        self.calendar1 = []
        self.calendar2 = []

    def book(self, start: int, end: int) -> bool:
        # one book
        calendar1 = self.calendar1
        # two books
        calendar2 = self.calendar2

        for book_start, book_end in calendar2:
            if (
                start < book_end and
                end > book_start
            ):
                return False

        for book_start, book_end in calendar1:
            if (
                start < book_end and
                end > book_start
            ):
                new_start = max(start, book_start)
                new_end = min(end, book_end)
                calendar2.append((new_start, new_end))

        calendar1.append((start, end))
        return True


myCalendarTwo = MyCalendarTwo()
print(myCalendarTwo.book(10, 20) == True)
print(myCalendarTwo.book(50, 60) == True)
print(myCalendarTwo.book(10, 40) == True)
print(myCalendarTwo.book(5, 15) == False)
print(myCalendarTwo.book(5, 10) == True)
print(myCalendarTwo.book(25, 55) == True)
