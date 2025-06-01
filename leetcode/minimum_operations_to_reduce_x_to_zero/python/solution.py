class Solution:
    def minOperations(self, numbers: list[int], x: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        target = sum(numbers) - x
        if target < 0:
            return -1
        elif target == 0:
            return len(numbers)
        
        left = 0
        window_sum = 0
        window_length = 0

        for right, number in enumerate(numbers):
            window_sum += number

            while left <= right and window_sum > target:
                window_sum -= numbers[left]
                left += 1
            
            if window_sum == target:
                window_length = max(window_length, right - left + 1)
        
        return (len(numbers) - window_length 
                if window_length 
                else -1)


print(Solution().minOperations([1, 1, 4, 2, 3], 5) == 2)
print(Solution().minOperations([5, 6, 7, 8, 9], 4) == -1)
print(Solution().minOperations([3, 2, 20, 1, 1, 3], 10) == 5)
print(Solution().minOperations([5, 2, 3, 1, 1], 5) == 1)
print(Solution().minOperations([1, 2], 3) == 2)
print(Solution().minOperations([1, 1], 3) == -1)
print(Solution().minOperations([8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], 134365) == 16)