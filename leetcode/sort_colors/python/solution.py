class Solution:
    def sortColors(self, numbers: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers, two pass
        """
        left = 0

        # move zeros left
        for right in range(len(numbers)):
            if numbers[right] == 0:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1
        
        # move ones left
        for right in range(left, len(numbers)):
            if numbers[right] == 1:
                numbers[left], numbers[right] = numbers[right], numbers[left]
                left += 1

        
        return numbers


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: bucket sort, two pass
        """
        bucket = [0] * 3  # i-th index is a frequency of i-th number
        
        for number in nums:
            bucket[number] += 1
        
        index = 0
        
        for number, frequency in enumerate(bucket):
            for _ in range(frequency):
                nums[index] = number
                index += 1
            
        return nums

class Solution:
    def sortColors(self, numbers: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers, three pointers, one pass
        """
        left = 0
        right = len(numbers) - 1
        index = 0

        while index <= right:
            if numbers[index] == 0:
                numbers[left], numbers[index] = numbers[index], numbers[left]
                left += 1

            elif numbers[index] == 2:
                numbers[index], numbers[right] = numbers[right], numbers[index]
                right -= 1
                index -= 1
            index += 1
        
        return numbers


print(Solution().sortColors([2, 0, 1]), [0, 1, 2])
print(Solution().sortColors([2, 0, 2, 1, 1, 0]), [0, 0, 1, 1, 2, 2])