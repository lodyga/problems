class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        """
        Time complexity: O(n+m)
        Auxiliary space complexity: O(n+m)
        Tags:
            DS: monotonic decreasing stack, hash map
            A: iteration
        """
        # {num: next greater num, ...}
        num2_next = {num: -1 for num in nums2}

        # Find the next greater number.
        stack = []  # decreasing stack
        for num in nums2:
            while stack and stack[-1] < num:
                num2_next[stack.pop()] = num

            stack.append(num)

        return [num2_next[num] for num in nums1]


print(Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1])
print(Solution().nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1])
print(Solution().nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]) == [7, 7, 7, 7, 7])
