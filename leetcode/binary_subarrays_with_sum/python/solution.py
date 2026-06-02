class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: sliding window
        """
        left = 0
        mid = 0
        res = 0

        for right, num in enumerate(nums):
            goal -= num

            while mid < right and goal < 0:
                goal += nums[mid]
                mid += 1
                left = mid

            while mid < right and nums[mid] == 0:
                mid += 1

            if goal == 0:
                res += (mid - left + 1)

        return res


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: prefix sum
        """
        # {prefix sum: freq}
        prefix_freq = {0: 1}
        prefix = 0
        res = 0

        for num in nums:
            prefix += num
            res += prefix_freq.get(prefix - goal, 0)
            prefix_freq[prefix] = prefix_freq.get(prefix, 0) + 1

        return res


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        res = 0

        for right in range(len(nums)):
            current_goal = goal

            for left in reversed(range(right + 1)):
                current_goal -= nums[left]

                if current_goal == 0:
                    res += 1
                elif current_goal < 0:
                    break

        return res


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        res = 0

        for right in range(len(nums)):
            for left in reversed(range(right + 1)):
                current_goal = nums[left: right + 1]

                if sum(current_goal) == goal:
                    res += 1
                elif sum(current_goal) > goal:
                    break

        return res


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4)
print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15)
print(Solution().numSubarraysWithSum([0, 1, 1, 0], 2) == 4)
print(Solution().numSubarraysWithSum([0, 1, 1, 0, 1], 2) == 5)
print(Solution().numSubarraysWithSum([0, 0, 1], 0) == 3)
print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 0) == 27)
print(Solution().numSubarraysWithSum([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 0) == 67)
