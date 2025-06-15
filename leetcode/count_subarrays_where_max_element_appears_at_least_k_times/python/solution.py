r"""
draft
[1, 3, 2, 3, 3]
[1,3,2,3], [3,2,3],        [1,3,2,3,3], [3,2,3,3], [2,3,3] and [3,3]

[1, 3, 2, 3, 1]
[1,3,2,3], [3,2,3],        [1,3,2,3,1], [3,2,3,1]
"""


class Solution:
    def countSubarrays(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        max_number = max(numbers)
        window = 0  # count occurences of the maximum number
        subarray_counter = 0  # count number of subsets

        for number in numbers:
            if number == max_number:
                window += 1

            while window == k:
                if numbers[left] == max_number:
                    window -= 1
                left += 1

            subarray_counter += left

        return subarray_counter


class Solution:
    def countSubarrays(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        subarray_counter = 0
        max_number = max(numbers)

        for i in range(len(numbers)):
            max_count = 0
           
            for j in range(i, len(numbers)):
                if numbers[j] == max_number:
                    max_count += 1
                if  max_count >= 2:
                    subarray_counter += 1

        return subarray_counter


print(Solution().countSubarrays([1, 3, 2, 3, 3], 2) == 6)
print(Solution().countSubarrays([1, 3, 2, 3, 3, 1], 2) == 10)
print(Solution().countSubarrays([1, 3, 2, 3, 1], 2) == 4)
print(Solution().countSubarrays([1, 3, 2, 3, 1, 1], 2) == 6)
print(Solution().countSubarrays([1, 3, 2, 3, 1, 1, 3], 2) == 10)
print(Solution().countSubarrays([1, 4, 2, 1], 3) == 0)
print(Solution().countSubarrays([3, 2, 3, 4, 4], 2) == 4)
print(Solution().countSubarrays([37, 20, 38, 66, 34, 38, 9, 41, 1, 14, 25, 63, 8, 12, 66, 66, 60, 12, 35, 27, 16, 38, 12, 66, 38, 36, 59, 54, 66, 54, 66, 48, 59, 66, 34, 11, 50, 66, 42, 51, 53, 66, 31, 24, 66, 44, 66, 1, 66, 66, 29, 54], 5) == 594)