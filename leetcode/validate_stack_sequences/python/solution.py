class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
            DS: stack
            A: two pointers
        """
        stack = []
        left = right = 0

        while left < len(pushed):
            stack.append(pushed[left])
            while stack and stack[-1] == popped[right]:
                stack.pop()
                right += 1
            left += 1

        return (
            left == len(pushed) and
            right == len(pushed)
        )


print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) == True)
print(Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) == False)
print(Solution().validateStackSequences([2, 1, 0], [1, 2, 0]) == True)
