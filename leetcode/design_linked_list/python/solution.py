class ListNode:
    def __init__(self, val=None, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    """
    Time complexity:
        constructor: O(1)
        get: O(n)
        addAtHead: O(1)
        addAtTail: O(n)
        addAtIndex: O(n)
        deleteAtIndex: O(n)
    Auxiliary space complexity O(n): 
    Tags: 
        DS: linked list, singly linked list
    """

    def __init__(self):
        self.anchor = ListNode()

    def get(self, index: int) -> int:
        node = self.anchor.next
        while index and node:
            node = node.next
            index -= 1
        return node.val if index == 0 and node else -1

    def addAtHead(self, val: int) -> None:
        self.anchor.next = ListNode(val, self.anchor.next)

    def addAtTail(self, val: int) -> None:
        node = self.anchor
        while node.next:
            node = node.next
        node.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        node = self.anchor
        while index and node.next:
            node = node.next
            index -= 1

        if index == 0:
            node.next = ListNode(val, node.next)

    def deleteAtIndex(self, index: int) -> None:
        node = self.anchor
        while index and node.next:
            node = node.next
            index -= 1

        if index == 0 and node.next:
            node.next = node.next.next


class DoublyListNode:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList2:
    def __init__(self):
        self.left = DoublyListNode()
        self.right = DoublyListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        node = self.left.next

        while index and node != self.right:
            node = node.next
            index -= 1

        if (index == 0 and node != self.right):
            return node.val
        else:
            return - 1

    def addAtHead(self, val: int) -> None:
        left = self.left
        right = self.left.next
        node = DoublyListNode(val, right, left)
        left.next = node
        right.prev = node

    def addAtTail(self, val: int) -> None:
        right = self.right
        left = self.right.prev
        node = DoublyListNode(val, right, left)
        right.prev = node
        left.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.left.next

        while index and next != self.right:
            next = next.next
            index -= 1

        if (index == 0 and next):
            prev = next.prev
            node = DoublyListNode(val, next, prev)
            prev.next = node
            next.prev = node

    def deleteAtIndex(self, index: int) -> None:
        node = self.left.next

        while index and node.next != self.right:
            node = node.next
            index -= 1

        if (
            node and index == 0 and
            node != self.right
        ):
            node.prev.next = node.next
            node.next.prev = node.prev


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
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
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
    ["MyLinkedList","deleteAtIndex"], 
    ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead","addAtHead","addAtHead","addAtHead","addAtHead","addAtTail","get","deleteAtIndex","deleteAtIndex"], 
    ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"],
    ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
]

arguments_list = [
    [[], [1], [3], [1, 2], [1], [1], [1]], 
    [[],[0]], 
    [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]], 
    [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]], 
    [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
]

expected_output_list = [
    [None, None, None, None, 2, None, 3], 
    [None, None], 
    [None, None, None, None, None, None, None, None, None, 2, None, None], 
    [None,None,None,None,2,None,3,-1,None,None,3,None,-1],
    [None,None,None,None,None,None,None,None,4,None,None,None]
]


# Run tests
def run_tests(
        operations_list: list[list[str]],
        arguments_list: list[list[list[int]]],
        expected_output_list: list[list[int | None]],
        show_output: bool = False
) -> list[bool]:
    """
    Run a batch of TimeMap tests and compare outputs with expected results.
    If show_output is True, returns [(actual, expected), ...] instead of booleans.
    """
    output = []
    for operations, arguments, expected_output in zip(operations_list, arguments_list, expected_output_list):
        if show_output:
            output.append((test_input(operations, arguments), expected_output))
        else:
            output.append(test_input(operations, arguments) == expected_output)
    return output


print(run_tests(operations_list, arguments_list, expected_output_list))


# Example 1
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)  # linked list becomes 1 -> 2 -> 3
print(myLinkedList.get(1))  # return 2
myLinkedList.deleteAtIndex(1)  # now the linked list is 1 -> 3
print(myLinkedList.get(1))  # return 3