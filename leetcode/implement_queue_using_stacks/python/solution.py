class MyQueue:
    """
    Time complexity: O(1)
        push: O(1)
        pop: O(1)
        peek: O(1)
        empty: O(1)
    Auxiliary space complexity: O(n)
    Tags: stack, queue
    """

    def __init__(self):
        self.stack = []
        self.reversed_stack = []

    def push(self, number: int) -> None:
        self.stack.append(number)

    def pop(self) -> int:
        self.reverse_stack()
        return self.reversed_stack.pop()

    def peek(self) -> int:
        self.reverse_stack()
        return self.reversed_stack[-1]

    def reverse_stack(self) -> None:
        if not self.reversed_stack:
            while self.stack:
                self.reversed_stack.append(self.stack.pop())

    def empty(self) -> bool:
        return (
            len(self.stack) == 0 and 
            len(self.reversed_stack) == 0)


myQueue = MyQueue()
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek())  # return 1
print(myQueue.pop())  # return 1, queue is [2]
print(myQueue.empty())  # return false