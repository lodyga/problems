class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        number_stack = []
        index = 0

        for number in pushed:
            number_stack.append(number)

            while number_stack and popped[index] == number_stack[-1]:
                number_stack.pop()
                index += 1

        return not number_stack and index == len(popped)


from collections import deque

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack, queue
        """
        number_stack = []
        queue = deque(popped)

        for number in pushed:
            number_stack.append(number)

            while number_stack and queue[0] == number_stack[-1]:
                number_stack.pop()
                queue.popleft()

        return not number_stack and not queue


class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        left = 0
        right = 0

        for number in pushed:
            pushed[left] = number
            left += 1

            while left and pushed[left - 1] == popped[right]:
                left -= 1
                right += 1
        
        return left == 0


print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) == True)
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) == False)
print(Solution().validateStackSequences([2, 1, 0], [1, 2, 0]) == True)