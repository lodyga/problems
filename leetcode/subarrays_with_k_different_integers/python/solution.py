class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: sliding window
        """
        left = 0
        right = 0
        num_freq = {}
        res = 0

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

            if len(num_freq) < k:
                continue

            if len(num_freq) > k:
                num_freq.pop(nums[right])
                right += 1
                left = right

            while num_freq[nums[right]] > 1:
                num_freq[nums[right]] -= 1
                right += 1

            res += right - left + 1

        return res


class Solution2:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: brute-force
        """
        res = 0
        
        for i in range(len(nums)):
            window = {}
            
            for j in range(i, len(nums)):
                window[nums[j]] = window.get(nums[j], 0) + 1
            
                if len(window) == k:
                    res += 1
        
        return res


print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2) == 7)
print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3) == 3)
