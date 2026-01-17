class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: backtracking
        """
        perm = []
        perms = []
        num_frequency = {}
        for num in nums:
            num_frequency[num] = num_frequency.get(num, 0) + 1

        def backtrack():
            if len(perm) == len(nums):
                perms.append(perm.copy())
                return
            
            for num in num_frequency:
                if num_frequency[num] == 0:
                    continue
                
                perm.append(num)
                num_frequency[num] -= 1
                backtrack()
                perm.pop()
                num_frequency[num] += 1

        backtrack()
        return perms


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: backtracking
        """
        nums.sort()
        perms = set()

        def backtrack(left):
            if left == len(nums):
                perms.add(tuple(nums))
                return
            
            for index in range(left, len(nums)):
                nums[left], nums[index] = nums[index], nums[left]
                backtrack(left + 1)
                nums[left], nums[index] = nums[index], nums[left]
        
        backtrack(0)
        return [list(perm) for perm in perms]


print(sorted(Solution().permuteUnique([1, 2])) == sorted([[1, 2], [2, 1]]))
print(sorted(Solution().permuteUnique([1, 2, 3])) == sorted([[1, 3, 2], [1, 2, 3], [2, 1, 3], [3, 2, 1], [3, 1, 2], [2, 3, 1]]))
print(sorted(Solution().permuteUnique([1])) == sorted([[1]]))
print(sorted(Solution().permuteUnique([1, 1, 2])) == sorted([[1, 2, 1], [2, 1, 1], [1, 1, 2]]))
print(sorted(Solution().permuteUnique([2, 2, 1, 1])) == sorted([[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]))
