r"""
draft
      -2     
    /    \    
  -2+1   1    
       /   \ 
     1-3    -3
     /  \
  -2+4   4
        /  \
      4-1   -1
      /  \
   3+2    2
  /   \
5+1    1 
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy (Kadane)
        """
        sub_sum = 0
        max_sub_sum = nums[0]

        for num in nums:
            sub_sum = sub_sum + num if sub_sum > 0 else num
            # sub_sum = max(sub_sum + num, num)
            max_sub_sum = max(max_sub_sum, sub_sum)

        return max_sub_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(Solution().maxSubArray([1]) == 1)
print(Solution().maxSubArray([5, 4, -1, 7, 8]) == 23)
print(Solution().maxSubArray([-4, -2, -1, -3]) == -1)
