# [3, 1, 2, 4]
#  3, 1, 1, 1
#     1, 1, 1
#        2, 2
#           4
#  17
class Solution:
    def sumSubarrayMins(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        MOD = 10**9 + 7
        N = len(nums)
        res = 0

        for left in range(N):
            min_val = nums[left]

            for right in range(left, N):
                min_val = min(min_val, nums[right])

                res = (res + min_val) % MOD

        return res


class Solution:
    def sumSubarrayMins(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        MOD = 10**9 + 7
        N = len(nums)
        res = 0

        for right in range(N):
            min_val = nums[right]

            for left in range(right, -1, -1):
                min_val = min(min_val, nums[left])

                res = (res + min_val) % MOD

        return res

# [3, 1, 2, 4]
#  3
#  1, 1
#  1, 1, 2
#  1, 1, 2, 4
# 17


class Solution:
    def sumSubarrayMins(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: monotonic increasing stack
            A: iteration
        """
        MOD = 10**9 + 7
        res = 0
        # increasing stack: stack([(num, count), ...])
        stack: list[tuple[int, int]] = []
        stack_sum = 0

        for num in nums:
            counter = 1

            while stack and stack[-1][0] > num:
                prev_num, prev_counter = stack.pop()
                stack_sum -= prev_num * prev_counter
                counter += prev_counter

            stack.append((num, counter))
            stack_sum += num * counter
            res = (res + stack_sum) % MOD

        return res


print(Solution().sumSubarrayMins([5, 4, 3]) == 22)
print(Solution().sumSubarrayMins([3, 1, 2, 4]) == 17)
print(Solution().sumSubarrayMins([11, 81, 94, 43, 3]) == 444)
