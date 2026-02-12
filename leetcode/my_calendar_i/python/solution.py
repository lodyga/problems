class LinkedNode:
    def __init__(self, start: int = 0, end: int = 0, next: int = 0) -> None:
        self.start = start
        self.end = end
        self.next = next


class MyCalendar:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: linked list
        A: interval, iteration
    """

    def __init__(self):
        self.calendar = LinkedNode()

    def book(self, start: int, end: int) -> bool:
        node = self.calendar

        while node.next:
            # New booking starts before current node.
            if end <= node.next.start:
                break

            # New booking starts after current node.
            elif node.next.end <= start:
                node = node.next

            # New booking overlaps current node.
            elif (
                start < node.next.end or
                end > node.next.start
            ):
                return False

        node.next = LinkedNode(start, end, node.next)
        return True


class TreeNode:
    def __init__(self, start=None, end=None, left=None, right=None) -> None:
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class MyCalendar:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: binary tree, BST
        A: interval, iteration
    """

    def __init__(self):
        self.calendar = None

    def book(self, start: int, end: int) -> bool:
        if self.calendar is None:
            self.calendar = TreeNode(start, end)
            return True

        node = self.calendar

        while True:
            # New booking starts after current node.
            if start >= node.end:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(start, end)
                    return True
            # New booking starts before current node.
            elif end <= node.start:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(start, end)
                    return True
            # New booking overlaps current node.
            else:
                return False


class MyCalendar:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: binary tree, BST
        A: interval, recursion
    """

    def __init__(self):
        self.calendar = None

    def book(self, start: int, end: int) -> bool:
        if self.calendar is None:
            self.calendar = TreeNode(start, end)
            return True
        else:
            return self._insert(self.calendar, start, end)

    def _insert(self, node, start, end) -> bool:
        if start >= node.end:
            if node.right:
                return self._insert(node.right, start, end)
            else:
                node.right = TreeNode(start, end)
                return True
        elif end <= node.start:
            if node.left:
                return self._insert(node.left, start, end)
            else:
                node.left = TreeNode(start, end)
                return True
        else:
            return False


class MyCalendar:
    def __init__(self):
        from sortedcontainers import SortedList
        self.events = SortedList()  # SortedList((start, end), )

    def book(self, start: int, end: int) -> bool:
        # Find the position where (start, end) would be inserted
        index = self.events.bisect_right((start, end))

        # Check if overlaps with previous event (at index - 1)
        if (
            index > 0 and
            start < self.events[index - 1][1]
        ):
            return False

        # Check if overlaps with next event (at idx)
        if (
            index < len(self.events) and
            end > self.events[index][0]
        ):
            return False

        self.events.add((start, end))
        return True


# Example 1
myCalendar = MyCalendar()
print(myCalendar.book(10, 20) == True)
print(myCalendar.book(15, 25) == False)
print(myCalendar.book(20, 30) == True)

# Example 2
myCalendar = MyCalendar()
print(myCalendar.book(47, 50) == True)
print(myCalendar.book(33, 41) == True)
print(myCalendar.book(39, 45) == False)
print(myCalendar.book(33, 42) == False)
print(myCalendar.book(25, 32) == True)
print(myCalendar.book(26, 35) == False)
print(myCalendar.book(19, 25) == True)
print(myCalendar.book(3, 8) == True)
print(myCalendar.book(8, 13) == True)
print(myCalendar.book(18, 27) == False)
