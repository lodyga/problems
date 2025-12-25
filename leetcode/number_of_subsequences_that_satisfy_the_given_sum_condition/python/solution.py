class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
            A: binary search, sorting
        """
        MOD = 10 ** 9 + 7
        counter = 0
        nums.sort()

        for index, num in enumerate(nums):
            if nums[index] * 2 > target:
                break

            # Default value for max_left must be index in case of
            # max_left = middle won't trigger
            max_left = index
            left = index + 1
            right = len(nums) - 1

            while left <= right:
                middle = (left + right) // 2
                middle_num = nums[middle]

                if num + middle_num > target:
                    right = middle - 1
                else:
                    max_left = middle
                    left = middle + 1

            counter += pow(2, max_left - index, MOD)
            counter %= MOD

        return counter


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: 
            A: two pointers, sorting
        """
        MOD = 10 ** 9 + 7
        counter = 0
        nums.sort()
        right = len(nums) - 1

        for left, left_num in enumerate(nums):
            while (
                left <= right and
                left_num + nums[right] > target
            ):
                right -= 1

            if left <= right:
                counter += pow(2, right - left, MOD)
                counter %= MOD

            if left == right:
                break

        return counter


print(Solution().numSubseq([3, 5, 6, 7], 9) == 4)
print(Solution().numSubseq([3, 3, 6, 8], 10) == 6)
print(Solution().numSubseq([2, 3, 3, 4, 6, 7], 12) == 61)
print(Solution().numSubseq([7, 10, 7, 3, 7, 5, 4], 12) == 56)
print(Solution().numSubseq([14, 4, 6, 6, 20, 8, 5, 6, 8, 12, 6, 10, 14, 9, 17, 16, 9, 7, 14, 11, 14, 15, 13, 11, 10, 18, 13, 17, 17, 14, 17, 7, 9, 5, 10, 13, 8, 5, 18, 20, 7, 5, 5, 15, 19, 14], 22) == 272187084)
print(Solution().numSubseq([9, 25, 9, 28, 24, 12, 17, 8, 28, 7, 21, 25, 10, 2, 16, 19, 12, 13, 15, 28, 14, 12, 24, 9, 6, 7, 2, 15, 19, 13, 30, 30, 23, 19, 11, 3, 17, 2, 14, 20, 22, 30, 12, 1, 11, 2, 2, 20, 20, 27, 15, 9, 10, 4, 12, 30, 13, 5, 2, 11, 29, 5, 3, 13, 22, 5, 16, 19, 7, 19, 11, 16, 11, 25, 29, 21, 29, 3, 2, 9, 20, 15, 9], 32) == 91931447)


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: two pointers
        """
        nums.sort()
        MOD = 10 ** 9 + 7
        counter = 0

        for left, left_num in enumerate(nums):
            if left_num * 2 > target:
                break
            
            right = left
            while (
                right < len(nums) and 
                left_num + nums[right] <= target
            ):
                right += 1
            
            counter += pow(2, right - left - 1, MOD)
            counter %= MOD

        return counter


# O(2^n), O(n)
# backtracking
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        counter = 0
        nums.sort()
        subsequence = []

        def dfs(index):
            nonlocal counter
            if index == len(nums):
                if (
                    subsequence and 
                    subsequence[0] + subsequence[-1] <= target
                ):
                    counter += 1
                    counter %= MOD
                return
            
            subsequence.append(nums[index])
            dfs(index + 1)
            subsequence.pop()
            dfs(index + 1)

        dfs(0)
        return counter


# O(2^n), O(n)
# backtracking
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        subsequence = []

        def dfs(index, counter):
            if index == len(nums):
                if (
                    subsequence and 
                    subsequence[0] + subsequence[-1] <= target
                ):
                    return 1
                else:
                    return 0
            
            subsequence.append(nums[index])
            left = dfs(index + 1, counter)
            subsequence.pop()
            right = dfs(index + 1, counter)
            return (left + right) % MOD

        return dfs(0, 0)
