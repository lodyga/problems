class Solution:
    def findLengthOfShortestSubarray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        # Find longest non-decreasing prefix.
        N = len(nums)
        left = 0
        right = N - 1
        
        while (
            left + 1 < N and
            nums[left] <= nums[left + 1]
        ):
            left += 1

        if (left == N - 1):
            return 0
            
        # Find longest non-decreasing suffix.
        while (
            right - 1 > -1 and
            nums[right - 1] <= nums[right]
        ):
            right -= 1

        res = min(N - 1 - left, right)

        # Try to merge prefix with suffix.
        l = 0
        r = right
        
        while (
            l <= left and
            r < N
        ):
            if nums[l] <= nums[r]:
                res = min(res, r - l - 1)
                l += 1
            else:
                r += 1
        
        return res


print(Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]) == 3)
print(Solution().findLengthOfShortestSubarray([5, 4, 3, 2, 1]) == 4)
print(Solution().findLengthOfShortestSubarray([1, 2, 3]) == 0)
print(Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 0, 7, 8, 9]) == 2)
