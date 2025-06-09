class Solution:
    def maxSubarrayLength(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(k)
        Tags: sliding window
        """
        window = {}  # {number: frequency}
        left = 0
        subarray_length = 0

        for right, number in enumerate(numbers):
            window[number] = window.get(number, 0) + 1

            while window[number] > k:
                left_number = numbers[left]
                window[left_number] -= 1

                if window[left_number] == 0:
                    del window[left_number]
                left += 1

            subarray_length = max(
                subarray_length,
                right - left + 1)

        return subarray_length


print(Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6)
print(Solution().maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) == 2)
print(Solution().maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) == 4)
print(Solution().maxSubarrayLength([1, 1, 2], 2) == 3)
print(Solution().maxSubarrayLength([1, 4, 4, 3], 1) == 2)