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
        Tags: greedy
        Kadane's Algorithm
        """
        total = 0
        max_sum = numbers[0]

        for number in numbers:
            total = total + number if total > 0 else number
            # total = max(total + number, number)
            # if total < 0:
            #     total = 0
            max_sum = max(max_sum, total)
        return max_sum


class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        Kadane's Algorithm, mutate imput list
        """
        for index in range(1, len(numbers)):
            numbers[index] += max(numbers[index - 1], 0)

        return max(numbers)


print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(Solution().maxSubArray([1]) == 1)
print(Solution().maxSubArray([5, 4, -1, 7, 8]) == 23)
print(Solution().maxSubArray([-4, -2, -1, -3]) == -1)
