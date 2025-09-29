class Solution:
    def longestMonotonicSubarray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        increaseing_len = 1
        decreaseing_len = 1
        max_len = 1

        for index in range(len(numbers) - 1):
            prev_number = numbers[index]
            number = numbers[index + 1]

            if prev_number < number:
                increaseing_len += 1
                decreaseing_len = 1
            elif prev_number > number:
                decreaseing_len += 1
                increaseing_len = 1
            else:
                decreaseing_len = 1
                increaseing_len = 1
            
            max_len = max(max_len, increaseing_len, decreaseing_len)
            
        return max_len


print(Solution().longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2)
print(Solution().longestMonotonicSubarray([3, 3, 3, 3]) == 1)
print(Solution().longestMonotonicSubarray([3, 2, 1]) == 3)