class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: sliding window
        """
        window = 0
        left = 0
        counter = 0
        max_num = max(nums)

        for num in nums:
            if num == max_num:
                window += 1

            while window == k:
                if nums[left] == max_num:
                    window -= 1
                left += 1

            counter += left

        return counter


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
            A: brute-force
        """
        counter = 0
        max_num = max(nums)

        for i in range(len(nums)):
            max_count = 0
           
            for j in range(i, len(nums)):
                if nums[j] == max_num:
                    max_count += 1
                if  max_count >= k:
                    counter += 1

        return counter


print(Solution().countSubarrays([1, 3, 2, 3, 3], 2) == 6)
print(Solution().countSubarrays([1, 3, 2, 3, 3, 1], 2) == 10)
print(Solution().countSubarrays([1, 3, 2, 3, 1], 2) == 4)
print(Solution().countSubarrays([1, 3, 2, 3, 1, 1], 2) == 6)
print(Solution().countSubarrays([1, 3, 2, 3, 1, 1, 3], 2) == 10)
print(Solution().countSubarrays([1, 4, 2, 1], 3) == 0)
print(Solution().countSubarrays([3, 2, 3, 4, 4], 2) == 4)
print(Solution().countSubarrays([37, 20, 38, 66, 34, 38, 9, 41, 1, 14, 25, 63, 8, 12, 66, 66, 60, 12, 35, 27, 16, 38, 12, 66, 38, 36, 59, 54, 66, 54, 66, 48, 59, 66, 34, 11, 50, 66, 42, 51, 53, 66, 31, 24, 66, 44, 66, 1, 66, 66, 29, 54], 5) == 594)
