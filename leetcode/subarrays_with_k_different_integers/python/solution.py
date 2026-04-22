class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: sliding window
        """
        # {number: frequency}
        num_freq = {}
        left = 0
        mid = 0
        counter = 0

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

            if len(num_freq) > k:
                num_freq.pop(nums[left])
                left += 1
                mid = left

            while num_freq[nums[left]] > 1:
                num_freq[nums[left]] -= 1
                left += 1

            if len(num_freq) == k:
                counter += left - mid + 1

        return counter


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: brute-force
        """
        counter = 0
        
        for i in range(len(nums)):
            window = {}
            
            for j in range(i, len(nums)):
                window[nums[j]] = window.get(nums[j], 0) + 1
                if len(window) == k:
                    counter += 1
        
        return counter


print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7)
print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3) == 3)
