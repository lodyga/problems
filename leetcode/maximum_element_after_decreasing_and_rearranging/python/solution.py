class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: greedy, sorting
        """
        nums.sort()
        max_num = 0

        for num in nums:
            if num > max_num:
                max_num += 1

        return max_num


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: greedy
        """
        N = len(nums)
        count = [0] * (N + 1)

        for num in nums:
            count[min(num, N)] += 1

        prev = 1
        for num in range(2, N + 1):
            prev = min(prev + count[num], num)

        return prev


print(Solution().maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]) == 2)
print(Solution().maximumElementAfterDecrementingAndRearranging([100, 1, 1000]) == 3)
print(Solution().maximumElementAfterDecrementingAndRearranging([1, 2, 3, 4, 5]) == 5)
print(Solution().maximumElementAfterDecrementingAndRearranging([73, 98, 9]))
print(Solution().maximumElementAfterDecrementingAndRearranging([73, 98, 9]) == 3)
print(Solution().maximumElementAfterDecrementingAndRearranging([5, 3, 3, 1]) == 4)
