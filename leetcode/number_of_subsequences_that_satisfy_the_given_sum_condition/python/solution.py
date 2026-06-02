class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: two pointers, sorting
        """
        MOD = 10 ** 9 + 7
        res = 0
        nums.sort()
        right = len(nums) - 1

        for left, left_num in enumerate(nums):
            while (
                left <= right and
                left_num + nums[right] > target
            ):
                right -= 1

            if left <= right:
                res += pow(2, right - left, MOD)
                res %= MOD

            if left == right:
                break

        return res


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: binary search, sorting
        """
        MOD = 10**9 + 7
        res = 0
        nums.sort()

        for left, left_num in enumerate(nums):
            if nums[left] * 2 > target:
                break

            right = left
            bs_left = left + 1
            bs_right = len(nums) - 1
            adjusted_target = target - left_num

            while bs_left <= bs_right:
                mid = (bs_left + bs_right) // 2
                mid_num = nums[mid]

                if mid_num > adjusted_target:
                    bs_right = mid - 1
                else:
                    right = mid
                    bs_left = mid + 1

            res += pow(2, right - left, MOD)
            res %= MOD

        return res


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: backtracking
        """
        MOD = 10 ** 9 + 7
        res = 0
        nums.sort()
        subseq = []

        def backtrack(idx):
            nonlocal res
            if idx == len(nums):
                if (
                    subseq and
                    subseq[0] + subseq[-1] <= target
                ):
                    res += 1
                    res %= MOD
                return

            subseq.append(nums[idx])
            backtrack(idx + 1)
            subseq.pop()
            backtrack(idx + 1)

        backtrack(0)
        return res


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: backtracking
        """
        MOD = 10 ** 9 + 7
        nums.sort()
        subseq = []

        def backtrack(idx, counter):
            if idx == len(nums):
                if (
                    subseq and
                    subseq[0] + subseq[-1] <= target
                ):
                    return 1
                else:
                    return 0

            subseq.append(nums[idx])
            left = backtrack(idx + 1, counter)
            subseq.pop()
            right = backtrack(idx + 1, counter)
            return (left + right) % MOD

        return backtrack(0, 0)


print(Solution().numSubseq([3, 5, 6, 7], 9) == 4)
print(Solution().numSubseq([3, 3, 6, 8], 10) == 6)
print(Solution().numSubseq([2, 3, 3, 4, 6, 7], 12) == 61)
print(Solution().numSubseq([7, 10, 7, 3, 7, 5, 4], 12) == 56)
print(Solution().numSubseq([14, 4, 6, 6, 20, 8, 5, 6, 8, 12, 6, 10, 14, 9, 17, 16, 9, 7, 14, 11, 14, 15, 13, 11, 10, 18, 13, 17, 17, 14, 17, 7, 9, 5, 10, 13, 8, 5, 18, 20, 7, 5, 5, 15, 19, 14], 22) == 272187084)
print(Solution().numSubseq([9, 25, 9, 28, 24, 12, 17, 8, 28, 7, 21, 25, 10, 2, 16, 19, 12, 13, 15, 28, 14, 12, 24, 9, 6, 7, 2, 15, 19, 13, 30, 30, 23, 19, 11, 3, 17, 2, 14, 20, 22, 30, 12, 1, 11, 2, 2, 20, 20, 27, 15, 9, 10, 4, 12, 30, 13, 5, 2, 11, 29, 5, 3, 13, 22, 5, 16, 19, 7, 19, 11, 16, 11, 25, 29, 21, 29, 3, 2, 9, 20, 15, 9], 32) == 91931447)
