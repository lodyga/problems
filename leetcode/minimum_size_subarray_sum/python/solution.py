class Solution:
    def minSubArrayLen(self, target: int, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        window_sum = 0
        window_length = len(numbers) + 1

        for right, number in enumerate(numbers):
            window_sum += number

            while window_sum > target:
                window_sum -= numbers[left]
                left += 1

            if window_sum == target:
                window_length = min(window_length, right - left + 1)

        return (window_length 
                if window_length != len(numbers) + 1 
                else 0)


print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]), 2)
print(Solution().minSubArrayLen(4, [1, 4, 4]), 1)
print(Solution().minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]), 0)