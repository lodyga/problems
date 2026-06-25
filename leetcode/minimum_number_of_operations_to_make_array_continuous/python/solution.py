class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sliding window, sorting
        """
        UNIQ_SORTED_NUMS = sorted(set(nums))
        N = len(nums)
        UNIQ_LEN = len(UNIQ_SORTED_NUMS)
        # matching num counter
        missing = 0
        right = 0

        for left, num in enumerate(UNIQ_SORTED_NUMS):
            while (
                right < UNIQ_LEN
                and num + N - 1 >= UNIQ_SORTED_NUMS[right]
            ):
                right += 1

            window_len = right - left
            missing = max(missing, window_len)

        return len(nums) - missing


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array, hash set
            A: brute-force, sliding window
        """
        N = len(nums)
        NUM_SET = set(nums)
        num_range = list(range(min(nums), max(nums) + 1))
        # missing num counter / min operations counter
        missing = 0
        res = N
        left = 0

        for right, num in enumerate(num_range):
            if num not in NUM_SET:
                missing += 1

            if right - left + 1 < N:
                continue

            res = min(res, missing)

            left_num = num_range[left]

            if left_num not in NUM_SET:
                missing -= 1

            left += 1

        return res


print(Solution().minOperations([4, 2, 5, 3]) == 0)
print(Solution().minOperations([1, 2, 3, 5, 6]) == 1)
print(Solution().minOperations([1, 10, 100, 1000]) == 3)
print(Solution().minOperations([2, 3, 5, 9]) == 1)
print(Solution().minOperations([1, 9, 10, 11, 19]) == 2)
print(Solution().minOperations([1, 3, 5, 7, 9]) == 2)
print(Solution().minOperations([8, 5, 9, 9, 8, 4]) == 2)
print(Solution().minOperations([8, 10, 16, 18, 10, 10, 16, 13, 13, 16]) == 6)
