class ListNode:
    def __init__(self, start=None, end=None, next=None):
        self.start = start
        self.end = end
        self.next = next


class MyCalendar:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags: linked list
    """
    def __init__(self):
        self.anchor = ListNode()

    def book(self, start: int, end: int) -> bool:
        node = self.anchor
        while node.next:
            # if intersection
            if (
                start < node.next.end and 
                end > node.next.start
            ):
                return False
            # if new booking before
            elif end <= node.next.start:
                break
            # if new booking after
            elif start >= node.next.end:
                node = node.next
        new_node = ListNode(start, end, node.next)
        node.next = new_node
        return True


class TreeNode:
    def __init__(self, start=None, end=None, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class MyCalendar:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags: binary tree, iteration
    """
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = TreeNode(start, end)
            return True
        
        node = self.root
        while node:
            if start >= node.end:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(start, end)
                    return True
            elif end <= node.start:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(start, end)
                    return True
            else:
                return False


class TreeNode:
    def __init__(self, start=None, end=None, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right


class MyCalendar:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags: binary tree, recursion
    """
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = TreeNode(start, end)
            return True
        
        return self._insert(self.root, start, end)

    def _insert(self, node, start, end):
        if start >= node.end:
            if node.right:
                return self._insert(node.right, start, end)
            else:
                node.right = TreeNode(start, end)
                return True
        elif end <= node.start:
            if node.left:
                return self._insert(node.left, start, end1)
            else:
                node.left = TreeNode(start, end)
                return True
        else:
            return False


from sortedcontainers import SortedList


class MyCalendar:
    def __init__(self):
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


myCalendar = MyCalendar()
print(myCalendar.book(10, 20))  # return True
print(myCalendar.book(15, 25))  # return False, It can not be booked because time 15 is already booked by another event.
print(myCalendar.book(20, 30))  # return True, The event can be booked, as the first event takes every time less than 20, but not including 20.