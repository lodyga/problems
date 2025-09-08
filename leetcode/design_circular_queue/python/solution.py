from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class MyCircularQueue:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags: linked list, queue
    """
    def __init__(self, k: int):
        self.size = 0
        self.size_limit = k
        self.anchor = ListNode()
        self.last_node = self.anchor

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.size += 1
        self.last_node.next = ListNode(value)
        self.last_node = self.last_node.next
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.anchor.next = self.anchor.next.next
        if self.isEmpty():
            self.last_node = self.anchor
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.anchor.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.last_node.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.size_limit


myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1))  # return True
print(myCircularQueue.enQueue(2))  # return True
print(myCircularQueue.enQueue(3))  # return True
print(myCircularQueue.enQueue(4))  # return False
print(myCircularQueue.Rear())  # return 3
print(myCircularQueue.isFull())  # return True
print(myCircularQueue.deQueue())  # return True
print(myCircularQueue.enQueue(4))  # return True
print(myCircularQueue.Rear())  # return 4


def test_input(operations: list[str], arguments: list[list[int | None]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "MyCircularQueue":
            cls = MyCircularQueue(*argument)
            output.append(None)
        elif operation == "enQueue":
            output.append(cls.enQueue(*argument))
        elif operation == "deQueue":
            output.append(cls.deQueue())
        elif operation == "Front":
            output.append(cls.Front())
        elif operation == "Rear":
            output.append(cls.Rear())
        elif operation == "isEmpty":
            output.append(cls.isEmpty())
        elif operation == "isFull":
            output.append(cls.isFull())

    return output


# Example Input
operations = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
arguments = [[3], [1], [2], [3], [4], [], [], [], [4], []]
expected_output = [None, True, True, True, False, 3, True, True, True, 4]

operations = ["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"]
arguments = [[6], [6], [], [], [], [5], [], [], [], [], [], []]
expected_output = [None, True, 6, 6, True, True, 5, True, -1, False, False, False]

# Run tests
actual_output = test_input(operations, arguments)
print(actual_output == expected_output)
print(actual_output)