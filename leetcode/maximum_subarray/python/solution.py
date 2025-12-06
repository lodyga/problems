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
    def maxSubArray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            A: greedy (Kadane)
        """
        subarray_sum = 0
        max_sum = numbers[0]

        for number in numbers:
            subarray_sum = subarray_sum + number if subarray_sum > 0 else number
            # subarray_sum = max(subarray_sum + number, number)
            # if subarray_sum < 0:
            #     subarray_sum = 0
            max_sum = max(max_sum, subarray_sum)
        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(Solution().maxSubArray([1]) == 1)
print(Solution().maxSubArray([5, 4, -1, 7, 8]) == 23)
print(Solution().maxSubArray([-4, -2, -1, -3]) == -1)
