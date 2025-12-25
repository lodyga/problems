class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: sliding window
        """
        far_left = 0
        left = 0
        counter = 0

        for right, num in enumerate(nums):
            goal -= num

            if left < right and goal < 0:
                goal += nums[left]
                left += 1
                far_left = left

            while left < right and nums[left] == 0:
                left += 1

            if goal == 0:
                counter += (left - far_left + 1)

        return counter


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: 
            A: brute-force
        """
        counter = 0

        for right in range(len(nums)):
            current_goal = goal

            for left in reversed(range(right + 1)):
                current_goal -= nums[left]

                if current_goal == 0:
                    counter += 1
                elif current_goal < 0:
                    break

        return counter


class Solution2:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(1)
        Tags: 
            A: brute-force
        """
        counter = 0

        for right in range(len(nums)):
            for left in reversed(range(right + 1)):
                current_goal = nums[left: right + 1]

                if sum(current_goal) == goal:
                    counter += 1
                elif sum(current_goal) > goal:
                    break

        return counter


class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_counter = {0: 1}  # {prefix: counter}
        prefix = 0
        counetr = 0

        for num in nums:
            prefix += num
            counetr += prefix_counter.get(prefix - goal, 0)
            prefix_counter[prefix] = prefix_counter.get(prefix, 0) + 1

        return counetr


print(Solution().numSubarraysWithSum([0, 1, 1, 0], 2) == 4)
print(Solution().numSubarraysWithSum([0, 1, 1, 0, 1], 2) == 5)
print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4)
print(Solution().numSubarraysWithSum([0, 0, 1], 0) == 3)
print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15)
print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 0) == 27)
print(Solution().numSubarraysWithSum([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 0) == 67)
