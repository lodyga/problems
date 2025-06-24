r"""
draft
[1, 3, 5, 4, 7]
[1, 1]      [[LIS lengths, frequency]]
   [2, 1]
      [3, 1]
         [3, 1]
            [4, 2]
"""


class Solution:
    def findNumberOfLIS(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        # [(increasing sequence length, frequency), ...]
        cache = [(1, 1) for _ in range(len(numbers))]
        lis_length = 1

        for right in range(len(numbers)):
            for left in range(right):
                if numbers[left] < numbers[right]:
                    prev_length, prev_frequency = cache[left]
                    # longer LIS found
                    if prev_length + 1 > cache[right][0]:
                        # update LIS length, carry frequencies to new LIS
                        cache[right] = (prev_length + 1, prev_frequency)
                        lis_length = max(lis_length, prev_length + 1)
                    # same length LIS found
                    elif prev_length + 1 == cache[right][0]:
                        # update LIS frequency
                        cache[right] = (cache[right][0], cache[right][1] + prev_frequency)


        return sum(frequency 
                   for subsequence_length, frequency in cache 
                   if subsequence_length == lis_length)


print(Solution().findNumberOfLIS([1, 3, 5, 4]) == 2)  # [1, 3, 4] and [1, 3, 5]
print(Solution().findNumberOfLIS([1, 3, 5, 4, 7]) == 2)  # [1, 3, 4, 7] and [1, 3, 5, 7]
print(Solution().findNumberOfLIS([2, 2, 2, 2, 2]) == 5)  # [2] * 5
print(Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]) == 3)  # [1, 2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 4, 5, 7]
print(Solution().findNumberOfLIS([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 27)