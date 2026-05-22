class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, in-place method
        """
        left = 0

        for right, num in enumerate(nums):
            if num % 2 == 0:
                nums[left], nums[right] = num, nums[left]
                left += 1

        return nums


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: queue
            A: iteration
        """
        from collections import deque
        queue = deque()

        for num in nums:
            if num % 2:
                queue.append(num)
            else:
                queue.appendleft(num)

        return list(queue)


print(Solution().sortArrayByParity([3, 1, 2, 4]), [2, 4, 3, 1])
print(Solution().sortArrayByParity([0]), [0])
print(Solution().sortArrayByParity([1, 2, 3, 4]), [2, 4, 3, 1])
