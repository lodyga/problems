class Solution:
    def findClosestElements(self, numbers: list[int], k: int, target: int) -> list[int]:
        """
        Time complexity: O(n-k)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        left = 0
        right = len(numbers) - 1


        while right - left + 1 > k:
            if target - numbers[left] <= numbers[right] - target:
                right -= 1
            else:
                left += 1
        
        return numbers[left: right + 1]


from collections import deque


class Solution:
    def findClosestElements(self, numbers: list[int], k: int, target: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: deque
        """
        queue = deque(numbers)
        
        while len(queue) > k:
            if target - queue[0] <= queue[-1] - target:
                queue.pop()
            else:
                queue.popleft()
        
        return list(queue)
            

class Solution:
    def findClosestElements(self, numbers: list[int], k: int, target: int) -> list[int]:
        """
        Time complexity: O(log(n-k))
        Auxiliary space complexity: O(1)
        Tags: binary search
        Starts with `sliding window` positioned in the middle of the `numbers`.
        Start binary search. If the first number outside of the `sliding window` 
        on the right minus `x` is less than `x` minus the first character 
        in the `sliding window` then search the right portion of the binary search.
        The solution on the right would be better than current `sliding window`.
        Else search the left portion of the binary search while preserving current 
        `sliding window` (current `sliding window` could be the solution).
        """
        left = 0
        right = len(numbers) - k

        while left < right:
            middle = (left + right) // 2
            if target - numbers[middle] <= numbers[middle + k] - target:
                right = middle
            else:
                left = middle + 1
        
        return numbers[left: left + k]


print(Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4])
print(Solution().findClosestElements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3])
print(Solution().findClosestElements([0, 1, 2, 2, 2, 3, 6, 8, 8, 9], 5, 9) == [3, 6, 8, 8, 9])