class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n!)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: backtracking
        """
        N = len(nums)
        perms = set()
        
        def backtrack(start: int) -> None:
            if start == N:
                perms.add(tuple(nums))
                return

            for idx in range(start, N):
                nums[idx], nums[start] = nums[start], nums[idx]
                backtrack(start + 1)
                nums[idx], nums[start] = nums[start], nums[idx]
            
        backtrack(0)
        return [list(perm) for perm in perms]


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
        res = []
        num_freq = {}
        
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        def backtrack():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for num in num_freq:
                if num_freq[num]:
                    perm.append(num)
                    num_freq[num] -= 1
                    backtrack()
                    num_freq[num] += 1
                    perm.pop()

        backtrack()
        return res


print(sorted(Solution().permuteUnique([1, 1, 2])), sorted([[1, 2, 1], [2, 1, 1], [1, 1, 2]]))
print(sorted(Solution().permuteUnique([1, 1, 2])) == sorted([[1, 2, 1], [2, 1, 1], [1, 1, 2]]))
print(sorted(Solution().permuteUnique([1, 2, 3])) == sorted([[1, 3, 2], [1, 2, 3], [2, 1, 3], [3, 2, 1], [3, 1, 2], [2, 3, 1]]))
print(sorted(Solution().permuteUnique([1, 2])) == sorted([[1, 2], [2, 1]]))
print(sorted(Solution().permuteUnique([1])) == sorted([[1]]))
print(sorted(Solution().permuteUnique([2, 2, 1, 1])) == sorted([[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]]))
