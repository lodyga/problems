class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        N = len(nums)
        totoal_ones = nums.count(1)
        left = 0
        window_ones = 0
        max_window_ones = 0

        for right in range(N*2):
            num = nums[right % N]

            if num:
                window_ones += 1

            if right - left + 1 < totoal_ones:
                continue

            max_window_ones = max(max_window_ones, window_ones)
            window_ones -= nums[left % N]
            left += 1

        return totoal_ones - max_window_ones


print(Solution().minSwaps([0, 1, 0, 1, 1, 0, 0]) == 1)
print(Solution().minSwaps([0, 1, 1, 1, 0, 0, 1, 1, 0]) == 2)
print(Solution().minSwaps([1, 1, 0, 0, 1]) == 0)
print(Solution().minSwaps([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]) == 1)
print(Solution().minSwaps([0, 0, 1, 0, 1, 1, 0, 1, 1, 1]) == 1)


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        N = len(nums)
        max_zeros = 0
        min_ones = N
        zeros_counter = 0
        ones_counter = 0

        for num in nums:
            if num:
                max_zeros = max(max_zeros, zeros_counter)
                ones_counter += 1
                zeros_counter = 0
            else:
                min_ones = min(min_ones, ones_counter)
                zeros_counter += 1

        max_zeros = max(max_zeros, zeros_counter)

        if max_zeros == N:
            return 0

        elif nums[0] == 0 and nums[-1] == 0:
            counter = 2
            left = 1
            right = N - 2

            while nums[left] == 0:
                counter += 1
                left += 1

            while nums[right] == 0:
                counter += 1
                right -= 1

            max_zeros = max(max_zeros, counter)

        return N - ones_counter - max_zeros


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        N = len(nums)
        ones_counter = nums.count(1)
        left = 0
        counter = 0
        min_zeros = N

        for right, num in enumerate(nums):
            if num == 0:
                counter += 1

            if right - left + 1 < ones_counter: # 1 - 0 + 1 < 3
                continue

            min_zeros = min(min_zeros, counter)

            if nums[left] == 0:
                counter -= 1
            
            left += 1

        return min_zeros


