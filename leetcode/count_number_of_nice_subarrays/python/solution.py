class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        left = 0
        mid = 0
        odd_counter = 0
        res = 0

        for right, num in enumerate(nums):
            if num % 2:
                odd_counter += 1

                if odd_counter == 1:
                    mid = right

                if odd_counter > k:
                    left = mid + 1
                    mid = left

                    while nums[mid] % 2 == 0:
                        mid += 1

            if odd_counter < k:
                continue

            res += (mid - left + 1)

        return res


print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2)
print(Solution().numberOfSubarrays([2, 4, 6], 1) == 0)
print(Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16)
print(Solution().numberOfSubarrays([1, 1, 1, 1, 1], 1) == 5)
print(Solution().numberOfSubarrays([91473, 45388, 24720, 35841, 29648, 77363, 86290, 58032, 53752, 87188, 34428, 85343, 19801, 73201], 4) == 6)
