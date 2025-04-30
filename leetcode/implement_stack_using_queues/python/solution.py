from collections import deque


class MyStack:
    """
    Time complexity:
        push: O(1)
        pop: O(n)
        top: O(n)
        empty: O(1)
    Auxiliary space complexity: O(n)
    Tags: queue, stack
    """

    def __init__(self):
        self.queue = deque()

    def push(self, number: int) -> None:
        self.queue.append(number)

    def pop(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        top_number = self.queue.popleft()
        self.queue.append(top_number)
        return top_number

    def empty(self) -> bool:
        return len(self.queue) == 0


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())  # return 2
print(myStack.pop())  # return 2
print(myStack.empty())  # return False