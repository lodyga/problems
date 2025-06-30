import heapq


class FreqStack:
    """
    Time complexity: 
        O(logn): push, pop
    Auxiliary space complexity: O(n)
    Tags: stack, heap
    """
    def __init__(self):
        self.min_heap = []  # [(-frequency, index, val), ...]
        self.number_frequency = {}  # {val: frequency, ...}
        self.index = 0

    def push(self, val: int) -> None:
        self.number_frequency[val] = self.number_frequency.get(val, 0) + 1
        heapq.heappush(self.min_heap, (-self.number_frequency[val], self.index, val))
        self.index -= 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.min_heap)
        self.number_frequency[val] -= 1
        return val


class FreqStack:
    """
    Time complexity: 
        O(1): push, pop
    Auxiliary space complexity: O(n)
    Tags: stack, hash map
    """
    def __init__(self):
        self.number_frequency = {}  # {number: frequency, ...}
        self.frequency_bucket = {}  # {frequency: [number, ...], ...}
        self.max_frequency = 0

    def push(self, number: int) -> None:
        self.number_frequency[number] = self.number_frequency.get(number, 0) + 1
        frequency = self.number_frequency[number]
        self.max_frequency = max(self.max_frequency, frequency)

        if frequency not in self.frequency_bucket:
            self.frequency_bucket[frequency] = []
        
        self.frequency_bucket[frequency].append(number)

    def pop(self) -> int:
        number = self.frequency_bucket[self.max_frequency].pop()
        self.number_frequency[number] -= 1
        
        if len(self.frequency_bucket[self.max_frequency]) == 0:
            del self.frequency_bucket[self.max_frequency]
            self.max_frequency -= 1

        return number


freqStack = FreqStack()
freqStack.push(5)  # The stack is [5]
freqStack.push(7)  # The stack is [5,7]
freqStack.push(5)  # The stack is [5,7,5]
freqStack.push(7)  # The stack is [5,7,5,7]
freqStack.push(4)  # The stack is [5,7,5,7,4]
freqStack.push(5)  # The stack is [5,7,5,7,4,5]
print(freqStack.pop())  # return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
print(freqStack.pop())  # return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
print(freqStack.pop())  # return 5, as 5 is the most frequent. The stack becomes [5,7,4].
print(freqStack.pop())  # return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].


def test_input(operations: list[str], arguments: list[list[int | None]]) -> list[list[int] | None]:
    result = []

    for operation, argument in zip(operations, arguments):
        if operation == "FreqStack":
            freqStack = FreqStack()
            result.append(None)
        elif operation == "push":
            freqStack.push(*argument)
            result.append(None)
        elif operation == "pop":
            result.append(freqStack.pop())
    
    return result

# Example Input
operations = ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
arguments = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
expected_output = [None, None, None, None, None, None, None, 5, 7, 5, 4]

operations = ["FreqStack","push","push","push","push","pop", "pop", "push", "push", "push", "pop", "pop", "pop"]
arguments = [[],[1], [1], [1], [2], [], [], [2], [2], [1], [], [], []]
expected_output = [None, None, None, None, None, 1, 1, None, None, None, 2, 1, 2]

# Run tests
actual_output = test_input(operations, arguments)
print(actual_output == expected_output)
# print(actual_output)





# O(1): push O(n): pop; aux space O(n)
# brute force
class FreqStack:
    def __init__(self):
        self.stack = []
        self.number_frequency = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.number_frequency[val] = self.number_frequency.get(val, 0) + 1

    def pop(self) -> int:
        max_frequency = max(self.number_frequency.values())
        reversed_stack = []

        while (self.stack and
               self.number_frequency[self.stack[-1]] != max_frequency):
            reversed_stack.append(self.stack.pop())

        most_frequent = self.stack.pop()
        self.number_frequency[most_frequent] -= 1

        while reversed_stack:
            self.stack.append(reversed_stack.pop())

        return most_frequent


from collections import defaultdict

# O(n), O(n)
# 2 default hash maps
class FreqStack:
    def __init__(self):
        self.number_frequency = defaultdict(int)  # {value: frequency, }
        self.frequency_bucket = defaultdict(list)  # {frequency: [value1, value2, ], }
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.number_frequency[val] += 1
        self.max_frequency = max(self.max_frequency, self.number_frequency[val])
        self.frequency_bucket[self.number_frequency[val]].append(val)

    def pop(self) -> int:
        val = self.frequency_bucket[self.max_frequency].pop()
        self.number_frequency[val] -= 1
        if not self.frequency_bucket[self.max_frequency]:
            self.max_frequency -= 1
        return val


from collections import defaultdict, deque

# O(n), O(n)
# 2 default hash maps, deque
class FreqStack:
    def __init__(self):
        self.number_frequency = defaultdict(int)  # {value: frequency, }
        self.frequency_bucket = defaultdict(deque)  # {frequency: deque(value1, value2, ), }
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.number_frequency[val] += 1
        self.max_frequency = max(self.max_frequency, self.number_frequency[val])
        self.frequency_bucket[self.number_frequency[val]].append(val)

    def pop(self) -> int:
        val = self.frequency_bucket[self.max_frequency].pop()
        self.number_frequency[val] -= 1
        if not self.frequency_bucket[self.max_frequency]:
            self.max_frequency -= 1
        return val