from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class MyLinkedList:
    """
    Time complexity:
        construct: O(1)
        addAtHead: O(1)
        addAtTail: O(n)
        addAtIndex: O(n)
        get: O(n)
        deleteAtIndex: O(n)
    Auxiliary space complexity O(n): 
    Tags: linked list
    singly linked list
    """

    def __init__(self):
        self.anchor = ListNode()

    def addAtHead(self, val: int) -> None:
        anchor = self.anchor
        new_head = ListNode(val, anchor.next)
        anchor.next = new_head

    def addAtTail(self, val: int) -> None:
        node = self.anchor
        while node.next:
            node = node.next

        new_tail = ListNode(val, None)
        node.next = new_tail

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.anchor
        while index and node.next:
            index -= 1
            node = node.next

        if index == 0:
            new_node = ListNode(val, node.next)
            node.next = new_node

    def get(self, index: int) -> int:
        node = self.anchor
        while index and node.next:
            index -= 1
            node = node.next

        return node.next.val if node.next and index == 0 else -1

    def deleteAtIndex(self, index: int) -> None:
        node = self.anchor
        while index and node.next:
            index -= 1
            node = node.next

        if index == 0 and node.next:
            node.next = node.next.next


myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)  # linked list becomes 1 -> 2 -> 3
print(myLinkedList.get(1))  # return 2
myLinkedList.deleteAtIndex(1)  # now the linked list is 1 -> 3
print(myLinkedList.get(1))  # return 3


def test_input(operations: list[str], arguments: list[list[int | None]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "MyLinkedList":
            cls = MyLinkedList(*argument)
            output.append(None)
        elif operation == "addAtHead":
            cls.addAtHead(*argument)
            output.append(None)
        elif operation == "addAtTail":
            cls.addAtTail(*argument)
            output.append(None)
        elif operation == "addAtIndex":
            cls.addAtIndex(*argument)
            output.append(None)
        elif operation == "deleteAtIndex":
            cls.deleteAtIndex(*argument)
            output.append(None)
        elif operation == "get":
            output.append(cls.get(*argument))

    return output


# Example Input
operations = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
arguments = [[], [1], [3], [1, 2], [1], [1], [1]]
expected_output = [None ,None ,None ,None ,2 ,None , 3]


# Run tests
actual_output = test_input(operations, arguments)
print(actual_output == expected_output)
print(actual_output)





# left <–> head <–> ... <–> node <–> ... <–> tail <–> right –> None
# O(n), O(n)
# linked list, doubly linked list
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:
    def __init__(self):
        self.left = ListNode()  # left dummy node
        self.right = ListNode()  # right dummy node
        self.left.next = self.right
        self.right.prev = self.left

    def addAtHead(self, val: int) -> None:
        next = self.left.next  # get old head
        prev = self.left  # get left dummy node
        node = ListNode(val, next, prev)  # create a new head
        prev.next = node  # point left dummy to new head
        next.prev = node  # point old head to new head

    def addAtTail(self, val: int) -> None:
        next = self.right  # get right dummy node
        prev = self.right.prev  # get old tail
        node = ListNode(val, next, prev)  # create a new tail
        prev.next = node  # point old tail to new tail
        next.prev = node  # point right dummy to new tail

    def get(self, index: int) -> int:
        node = self.left.next  # get head node

        while index and node != self.right:  # while index > 0 and not on right node
            node = node.next  # next node
            index -= 1  # next index

        if (index == 0 and
                node != self.right):  # not on right node
            return node.val
        else:
            return - 1

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.left.next  # get head node

        while index and next != self.right:  # while index > 0 and next not on None
            next = next.next  # next node
            index -= 1  # next index

        if (index == 0 and next):  # not on right node
            prev = next.prev  # get previous node
            node = ListNode(val, next, prev)  # create a new node between next and previous nodes
            prev.next = node  # point previous node to new node
            next.prev = node  # point next node to new node

    def deleteAtIndex(self, index: int) -> None:
        node = self.left.next  # get head node

        while index and node.next != self.right:  # while index > 0 and next not on None
            node = node.next  # next node
            index -= 1  # next index

        if (node and index == 0 and 
                node != self.right):
            node.prev.next = node.next  # point previous node to next node
            node.next.prev = node.prev  # poion next node to previous node
