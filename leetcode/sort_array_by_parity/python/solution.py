class Solution:
    def sortArrayByParity(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: in-place method, two pointers
        """
        left = 0
        for right in range(len(numbers)):
            if not numbers[right] % 2:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1

        return numbers


from collections import deque


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


print(Solution().sortArrayByParity([3, 1, 2, 4]), [2, 4, 3, 1])
print(Solution().sortArrayByParity([1, 2, 3, 4]), [2, 4, 3, 1])
print(Solution().sortArrayByParity([0]), [0])