class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: sliding window
        """
        total = sum(nums)
        if total == x:
            return len(nums)
        target = total - x
        # find max window length
        window_length = 0
        window = 0
        left = 0

        for right, num in enumerate(nums):
            window += num

            while (
                left < right and
                window > target
            ):
                window -= nums[left]
                left += 1

            if window == target:
                window_length = max(window_length, right - left + 1)

        return len(nums) - window_length if window_length else -1


print(Solution().minOperations([1, 1, 4, 2, 3], 5) == 2)
print(Solution().minOperations([5, 6, 7, 8, 9], 4) == -1)
print(Solution().minOperations([3, 2, 20, 1, 1, 3], 10) == 5)
print(Solution().minOperations([5, 2, 3, 1, 1], 5) == 1)
print(Solution().minOperations([1, 2], 3) == 2)
print(Solution().minOperations([1, 1], 3) == -1)
print(Solution().minOperations([8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309], 134365) == 16)
