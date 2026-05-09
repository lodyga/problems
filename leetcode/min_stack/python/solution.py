class MinStack:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(n)
    Tags:
        DS: stack
        A: iteration
    """

    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin() == -3)
minStack.pop()
print(minStack.top() == 0)
print(minStack.getMin() == -2)
