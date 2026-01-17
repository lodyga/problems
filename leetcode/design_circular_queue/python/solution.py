class DoublyLinkedNode:
    def __init__(self, val=None, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class MyCircularQueue:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: queue, doubly linked list
    """
    def __init__(self, cap: int):
        self.cap = cap
        self.size = 0
        self.left = DoublyLinkedNode()
        self.right = DoublyLinkedNode(None, None, self.left)
        self.left.next = self.right

    def enQueue(self, val: int) -> bool:
        if self.isFull():
            return False
        
        right = self.right
        left = right.prev
        node = DoublyLinkedNode(val, right, left)
        left.next = node
        right.prev = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        left = self.left
        right = self.left.next.next
        left.next = right
        right.prev = left
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap


class ListNode:
    """
    Definition for singly-linked list.
    """
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: queue, linked list
    """
    def __init__(self, cap: int):
        self.cap = cap
        self.size = 0
        self.anchor = ListNode()
        self.last_node = self.anchor

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.last_node.next = ListNode(value)
        self.last_node = self.last_node.next
        self.size += 1
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
        return self.size == self.cap


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
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
            output.append(cls.deQueue(*argument))
        elif operation == "Front":
            output.append(cls.Front(*argument))
        elif operation == "Rear":
            output.append(cls.Rear(*argument))
        elif operation == "isEmpty":
            output.append(cls.isEmpty(*argument))
        elif operation == "isFull":
            output.append(cls.isFull(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"],
    ["MyCircularQueue","enQueue","Rear","Rear","deQueue","enQueue","Rear","deQueue","Front","deQueue","deQueue","deQueue"],
    ["MyCircularQueue","enQueue","deQueue","enQueue","enQueue","deQueue","isFull","isFull","Front","deQueue","enQueue","Front","enQueue","enQueue","Rear","Rear","deQueue","enQueue","enQueue","Rear","Rear","Front","Rear","Rear","deQueue","enQueue","Rear","deQueue","Rear","Rear","Front","Front","enQueue","enQueue","Front","enQueue","enQueue","enQueue","Front","isEmpty","enQueue","Rear","enQueue","Front","enQueue","enQueue","Front","enQueue","deQueue","deQueue","enQueue","deQueue","Front","enQueue","Rear","isEmpty","Front","enQueue","Front","deQueue","enQueue","enQueue","deQueue","deQueue","Front","Front","deQueue","isEmpty","enQueue","Rear","Front","enQueue","isEmpty","Front","Front","enQueue","enQueue","enQueue","Rear","Front","Front","enQueue","isEmpty","deQueue","enQueue","enQueue","Rear","deQueue","Rear","Front","enQueue","deQueue","Rear","Front","Rear","deQueue","Rear","Rear","enQueue","enQueue","Rear","enQueue"]
]

arguments_list = [
    [[3],[1],[2],[3],[4],[],[],[],[4],[]],
    [[6],[6],[],[],[],[5],[],[],[],[],[],[]],
    [[81],[69],[],[92],[12],[],[],[],[],[],[28],[],[13],[45],[],[],[],[24],[27],[],[],[],[],[],[],[88],[],[],[],[],[],[],[53],[39],[],[28],[66],[17],[],[],[47],[],[87],[],[92],[94],[],[59],[],[],[99],[],[],[84],[],[],[],[52],[],[],[86],[30],[],[],[],[],[],[],[45],[],[],[83],[],[],[],[22],[77],[23],[],[],[],[14],[],[],[90],[57],[],[],[],[],[34],[],[],[],[],[],[],[],[49],[59],[],[71]]
]

expected_output_list = [
    [None, True, True, True, False, 3, True, True, True, 4],
    [None, True, 6, 6, True, True, 5, True, -1, False, False, False],
    [None, True, True, True, True, True, False, False, 12, True, True, 28, True, True, 45, 45, True, True, True, 27, 27, 13, 27, 27, True, True, 88, True, 88, 88, 24, 24, True, True, 24, True, True, True, 24, False, True, 47, True, 24, True, True, 24, True, True, True, True, True, 53, True, 84, False, 53, True, 53, True, True, True, True, True, 66, 66, True, False, True, 45, 17, True, False, 17, 17, True, True, True, 23, 17, 17, True, False, True, True, True, 57, True, 57, 87, True, True, 34, 92, 34, True, 34, 34, True, True, 59, True]
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
myCircularQueue = MyCircularQueue(3)
print(myCircularQueue.enQueue(1) == True)
print(myCircularQueue.enQueue(2) == True)
print(myCircularQueue.enQueue(3) == True)
print(myCircularQueue.enQueue(4) == False)
print(myCircularQueue.Rear() == 3)
print(myCircularQueue.isFull() == True)
print(myCircularQueue.deQueue() == True)
print(myCircularQueue.enQueue(4) == True)
print(myCircularQueue.Rear() == 4)
