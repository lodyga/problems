class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: iteration
        """
        prev_num = nums[0]
        inc_len = 1
        dec_len = 1
        max_monot_len = 1

        for index in range(1, len(nums)):
            num = nums[index]

            if prev_num < num:
                inc_len += 1
                max_monot_len = max(max_monot_len, inc_len)
                dec_len = 1
            elif prev_num > num:
                dec_len += 1
                max_monot_len = max(max_monot_len, dec_len)
                inc_len = 1
            else:
                dec_len = 1
                inc_len = 1

            prev_num = num

        return max_monot_len


print(Solution().longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2)
print(Solution().longestMonotonicSubarray([3, 3, 3, 3]) == 1)
print(Solution().longestMonotonicSubarray([3, 2, 1]) == 3)
print(Solution().longestMonotonicSubarray([3]) == 1)
