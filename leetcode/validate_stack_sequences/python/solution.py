class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack
            A: two pointers
        """
        idx2 = 0
        stack = []

        for num1 in pushed:
            stack.append(num1)

            while stack and stack[-1] == popped[idx2]:
                stack.pop()
                idx2 += 1

        return (
            len(stack) == 0 and
            idx2 == len(popped)
        )


print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) == True)
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) == False)
print(Solution().validateStackSequences([2, 1, 0], [1, 2, 0]) == True)
