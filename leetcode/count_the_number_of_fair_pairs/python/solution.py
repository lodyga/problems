class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        N = len(nums)
        nums.sort()
        mid = 1
        mid_num = nums[mid]
        right = N - 1
        right_num = nums[right]
        res = 0
        
        for left in range(N - 1):
            left_num = nums[left]
            mid = max(mid, left + 1)

            while mid < N and left_num + nums[mid] < lower:
                mid += 1
            
            while mid <= right and left_num + nums[right] > upper:
                right -= 1
            
            if mid > right:
                break

            res += (right - mid + 1)

        return res


# [0, 1, 4, 4, 5, 7]

# [1, 2, 5, 7, 9]
# 

print(Solution().countFairPairs([1, 7, 9, 2, 5], 11, 11), 1)
print(Solution().countFairPairs([0, 1, 7, 4, 4, 5], 3, 6), 6)
