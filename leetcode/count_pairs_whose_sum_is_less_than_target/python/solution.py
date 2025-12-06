class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
            A: two pointers, sorting
        """
        nums.sort()
        counter = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] < target:
                counter += right - left
                left += 1
            else:
                right -= 1

        return counter


class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags: brute-force
        """
        nums.sort()
        counter = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    counter += 1
                else:
                    break
        return counter


print(Solution().countPairs([1, 1, 3, 4, 5], 6) == 5)
print(Solution().countPairs([-1, 1, 2, 3, 1], 2) == 3)
print(Solution().countPairs([-6, 2, 5, -2, -7, -1, 3], -2) == 10)
print(Solution().countPairs([6, -1, 7, 4, 2, 3], 8) == 8)
print(Solution().countPairs([-5, 0, -7, -1, 9, 8, -9, 9], -14) == 1)
