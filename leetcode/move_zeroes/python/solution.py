class Solution:
    def moveZeroes(self, numbers: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers, in-place method
        """
        left = 0

        for right, number in enumerate(numbers):
            if number != 0:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1
        
        return numbers
            

print(Solution().moveZeroes([0]), [0])
print(Solution().moveZeroes([1]), [1])
print(Solution().moveZeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])