class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n)
        Tags: 
            A: two pointers
        """
        nums.sort()
        quadruplets = []

        for i in range(0, len(nums) - 3):
            # if not the first i loop
            # skip repeating nums
            if i and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums) - 2):
                # if not the first j loop
                # skip repeating nums
                if j != i + 1 and nums[j - 1] == nums[j]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    quadruplet = nums[i] + nums[j] + nums[left] + nums[right]

                    if quadruplet == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif quadruplet < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets


print(sorted(Solution().fourSum([1, 0, -1, 0, -2, 2], 0)) == sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))
print(sorted(Solution().fourSum([2, 2, 2, 2, 2], 8)) == sorted([[2, 2, 2, 2]]))
print(sorted(Solution().fourSum([0, 0, 0, 0], 0)) == sorted([[0, 0, 0, 0]]))
print(sorted(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11)) == sorted([[-5, -4, -3, 1]]))
