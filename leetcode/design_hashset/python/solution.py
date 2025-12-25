from linked_list_utils import *


# class ListNode:
#     """
#     Definition for singly-linked list.
#     """
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next


class MyHashSet:
    """
    Time complexity:
        constructor: O(n)
        add: O(1)
        contains: O(1)
        remove: O(1)
    Auxiliary space complexity: O(n)
    Tags: 
        DS: linked list, hash set
        A: iteration
    """

    def __init__(self):
        self.set = [ListNode() for _ in range(10**4)]
    
    def _get_hash(self, key: int) -> int:
        return key % len(self.set)

    def add(self, key: int) -> None:
        if not self.contains(key):
            index = self._get_hash(key)
            node = self.set[index]
            node.next = ListNode(key, node.next)
            return

    def remove(self, key: int) -> None:
        index = self._get_hash(key)
        node = self.set[index]

        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                return
            node = node.next

    def contains(self, key: int) -> bool:
        index = self._get_hash(key)
        node = self.set[index]

        while node.next:
            if node.next.val == key:
                return True
            node = node.next
        return False


def test_input(operations: list[str], arguments: list[list[int]]) -> list[int | None]:
    """
    Test input provided in two separate lists: operations and arguments
    """
    cls = None
    output = []

    for operation, argument in zip(operations, arguments):
        if operation == "MyHashSet":
            cls = MyHashSet(*argument)
            output.append(None)
        elif operation == "add":
            cls.add(*argument)
            output.append(None)
        elif operation == "remove":
            cls.remove(*argument)
            output.append(None)
        elif operation == "contains":
            output.append(cls.contains(*argument))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return output


# Example Input
operations_list = [
    ["MyHashSet","add","add","contains","contains","add","contains","remove","contains"],
    ["MyHashSet","contains","remove","add","add","contains","remove","contains","contains","add","add","add","add","remove","add","add","add","add","add","add","add","add","add","add","contains","add","contains","add","add","contains","add","add","remove","add","add","add","add","add","contains","add","add","add","remove","contains","add","contains","add","add","add","add","add","contains","remove","remove","add","remove","contains","add","remove","add","add","add","add","contains","contains","add","remove","remove","remove","remove","add","add","contains","add","add","remove","add","add","add","add","add","add","add","add","remove","add","remove","remove","add","remove","add","remove","add","add","add","remove","remove","remove","add","contains","add"]
]

arguments_list = [
    [[],[1],[2],[1],[3],[2],[2],[2],[2]],
    [[],[72],[91],[48],[41],[96],[87],[48],[49],[84],[82],[24],[7],[56],[87],[81],[55],[19],[40],[68],[23],[80],[53],[76],[93],[95],[95],[67],[31],[80],[62],[73],[97],[33],[28],[62],[81],[57],[40],[11],[89],[28],[97],[86],[20],[5],[77],[52],[57],[88],[20],[48],[42],[86],[49],[62],[53],[43],[98],[32],[15],[42],[50],[19],[32],[67],[84],[60],[8],[85],[43],[59],[65],[40],[81],[55],[56],[54],[59],[78],[53],[0],[24],[7],[53],[33],[69],[86],[7],[1],[16],[58],[61],[34],[53],[84],[21],[58],[25],[45],[3]]
]

expected_output_list = [
    [None, None, None, True, False, None, True, None, False],
    [None,False,None,None,None,False,None,True,False,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,False,None,True,None,None,True,None,None,None,None,None,None,None,None,True,None,None,None,None,False,None,False,None,None,None,None,None,True,None,None,None,None,True,None,None,None,None,None,None,True,True,None,None,None,None,None,None,None,False,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,False,None]
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
myHashSet = MyHashSet()
myHashSet.add(1)  # set = [1]
myHashSet.add(2)  # set = [1, 2]
print(myHashSet.contains(1))  # return True
print(myHashSet.contains(3))  # return False, (not found)
myHashSet.add(2)  # set = [1, 2]
print(myHashSet.contains(2))  # return True
myHashSet.remove(2)  # set = [1]
print(myHashSet.contains(2))  # return False, (already removed)