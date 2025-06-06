class Solution:
    def numSubarraysWithSum(self, numbers: list[int], goal: int) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        left = 0
        middle = 0
        subarray_counter = 0

        for right in range(len(numbers)):
            goal -= numbers[right]

            while middle < right and goal < 0:
                goal += numbers[middle]
                middle += 1
                left = middle

            if goal == 0:
                while middle < right and numbers[middle] == 0:
                    middle += 1
                subarray_counter += (middle - left + 1)

        return subarray_counter


class Solution:
    def numSubarraysWithSum(self, numbers: list[int], goal: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        subarray_counter = 0

        for right in range(len(numbers)):
            current_goal = goal
            
            for left in reversed(range(right + 1)):
                current_goal -= numbers[left]
                if current_goal == 0:
                    subarray_counter += 1
                elif current_goal < 0:
                    break

        return subarray_counter


class Solution:
    def numSubarraysWithSum(self, numbers: list[int], goal: int) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        subarray_counter = 0

        for right in range(len(numbers)):
            for left in reversed(range(right + 1)):
                current_goal = numbers[left: right + 1]
                
                if sum(current_goal) == goal:
                    subarray_counter += 1
                elif sum(current_goal) > goal:
                    break

        return subarray_counter


print(Solution().numSubarraysWithSum([0, 1, 1, 0], 2) == 4)
print(Solution().numSubarraysWithSum([0, 1, 1, 0, 1], 2) == 5)
print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2) == 4)
print(Solution().numSubarraysWithSum([0, 0, 1], 0) == 3)
print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0], 0) == 15)
print(Solution().numSubarraysWithSum([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 0) == 27)