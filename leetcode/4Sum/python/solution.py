class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n)
        Tags:
            A: two pointers
        """
        nums.sort()
        N = len(nums)
        res = []

        for i in range(N - 3):
            # if not the first i loop
            # skip repeating nums
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            for j in range(i + 1, N - 2):
                # if not the first j loop
                # skip repeating nums
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                
                left = j + 1
                right = N - 1
                
                while left < right:
                    quad = nums[i] + nums[j] + nums[left] + nums[right]

                    if target == quad:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                        
                    elif target < quad:
                        right -= 1
                    else:
                        left += 1

        return res


print(sorted(Solution().fourSum([1, 0, -1, 0, -2, 2], 0)) == sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]))
print(sorted(Solution().fourSum([2, 2, 2, 2, 2], 8)) == sorted([[2, 2, 2, 2]]))
print(sorted(Solution().fourSum([0, 0, 0, 0], 0)) == sorted([[0, 0, 0, 0]]))
print(sorted(Solution().fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11)) == sorted([[-5, -4, -3, 1]]))
