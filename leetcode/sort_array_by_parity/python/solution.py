from collections import deque


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
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums


class Solution:
    def sortArrayByParity(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: queue
        """
        queue = deque()

        for number in numbers:
            if number % 2:
                queue.append(number)
            else:
                queue.appendleft(number)

        return list(queue)


print(Solution().sortArrayByParity([3, 1, 2, 4]) == [2, 4, 3, 1])
print(Solution().sortArrayByParity([1, 2, 3, 4]) == [2, 4, 3, 1])
print(Solution().sortArrayByParity([0]) == [0])
