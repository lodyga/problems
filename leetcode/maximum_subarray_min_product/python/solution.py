class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: brute-force, prefix sum
        """
        MOD = 10**9 + 7
        nums_len = len(nums)
        res = nums[0]

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        for left in range(nums_len):
            min_num = nums[left]
            subarray_sum = 0

            for right in range(left, nums_len):
                min_num = min(min_num, nums[right])
                subarray_sum = prefix[right + 1] - prefix[left]
                res = max(res, min_num * subarray_sum % MOD)

        return res


class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: iteration
        """
        MOD = 10**9 + 7
        res = nums[0]
        stack = []

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        for index, num in enumerate(nums):
            start = index

            while stack and stack[-1][1] > num:
                start, val = stack.pop()
                subarray_sum = prefix[index] - prefix[start]
                res = max(res, val * subarray_sum)

            stack.append((start, num))

        while stack:
            index, val = stack.pop()
            subarray_sum = prefix[len(nums)] - prefix[index]
            res = max(res, val * subarray_sum)

        return res % MOD


print(Solution().maxSumMinProduct([1]) == 1)
print(Solution().maxSumMinProduct([1, 2]) == 4)
print(Solution().maxSumMinProduct([1, 2, 3]) == 10)
print(Solution().maxSumMinProduct([1, 2, 3, 2]) == 14)
print(Solution().maxSumMinProduct([2, 3, 3, 1, 2]) == 18)
print(Solution().maxSumMinProduct([3, 1, 5, 6, 4, 2]) == 60)
