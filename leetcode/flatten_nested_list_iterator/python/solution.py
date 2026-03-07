"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


from collections import deque


# class NestedInteger:
#     def isInteger(self) -> bool:
#         """
#         @return True if this NestedInteger holds a single integer, rather than a nested list.
#         """
#     def getInteger(self) -> int:
#         """
#         @return the single integer that this NestedInteger holds, if it holds a single integer
#         Return None if this NestedInteger holds a nested list
#         """
#     def getList(self) -> [NestedInteger]:
#         """
#         @return the nested list that this NestedInteger holds, if it holds a nested list
#         Return None if this NestedInteger holds a single integer
#         """


class NestedInteger:
    def __init__(self, value):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:  # assume list
            self._integer = None
            self._list = [NestedInteger(v) for v in value]

    def isInteger(self) -> bool:
        return self._integer is not None

    def getInteger(self) -> int:
        return self._integer

    def getList(self):
        return self._list


class NestedIterator:
    """
        Time complexity: O(n)
            n: integer count
            d: recursion depth
        Auxiliary space complexity: O(d)
        Tags:
            DS: stack
            A: recursion
        """

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self._flatten_list(nestedList)
        self.stack.reverse()

    def _flatten_list(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                self.stack.append(item.getInteger())
            else:  # if List
                self._flatten_list(item.getList())

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class NestedIterator:
    """
        Time complexity: O(n)
            n: integer count
            d: recursion depth
        Auxiliary space complexity: O(d)
        Tags:
            DS: queue
            A: recursion
        """

    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque()
        self._flatten_list(nestedList)

    def _flatten_list(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                self.queue.append(item.getInteger())
            else:  # if List
                self._flatten_list(item.getList())

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue) > 0

    """
        Time complexity: O(n)
            n: integer count
            d: recursion depth
        Auxiliary space complexity: O(1)
        Tags:
            A: recursion
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stop_gen = object()
        self.int_generator = self._generate_int(nestedList)
        self.next_int = next(self.int_generator, self.stop_gen)

    def _generate_int(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                yield item.getInteger()
            else:  # if List
                yield from self._generate_int(item.getList())

    def next(self) -> int:
        res = self.next_int
        self.next_int = next(self.int_generator, self.stop_gen)
        return res

    def hasNext(self) -> bool:
        return self.next_int is not self.stop_gen



nested = [NestedInteger([1, 1]),
          NestedInteger(2),
          NestedInteger([1, 1])]

iterator = NestedIterator(nested)

result = []
while iterator.hasNext():
    result.append(iterator.next())
print(result)