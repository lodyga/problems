class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sliding window, sorting
        """
        uniq_sort_nums = sorted(set(nums))
        # matching num counter
        max_window = 0
        right = 0
        num_len = len(nums)

        for left, num in enumerate(uniq_sort_nums):
            while (
                right < len(uniq_sort_nums) and
                num + num_len - 1 >= uniq_sort_nums[right]
            ):
                right += 1

            window = right - left
            max_window = max(max_window, window)

        return num_len - max_window


class Solution2:
    def minOperations(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, hash set
            A: brute-force, sliding window
        """
        num_set = set(nums)
        num_range = list(range(min(nums), max(nums) + 1))
        # missing num counter / min operations counter
        window = 0
        min_window = len(nums)
        left = 0

        for right, num in enumerate(num_range):
            if num not in num_set:
                window += 1

            if right - left + 1 < len(nums):
                continue

            min_window = min(min_window, window)

            left_num = num_range[left]
            if left_num not in num_set:
                window -= 1
            left += 1

        return min_window


print(Solution().minOperations([2, 3, 5, 9]) == 1)
print(Solution().minOperations([4, 2, 5, 3]) == 0)
print(Solution().minOperations([1, 2, 3, 5, 6]) == 1)
print(Solution().minOperations([1, 10, 100, 1000]) == 3)
print(Solution().minOperations([1, 9, 10, 11, 19]) == 2)
print(Solution().minOperations([1, 3, 5, 7, 9]) == 2)
print(Solution().minOperations([8, 5, 9, 9, 8, 4]) == 2)
print(Solution().minOperations([8, 10, 16, 18, 10, 10, 16, 13, 13, 16]) == 6)
