class Solution:
    def maxScoreSightseeingPair(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        prev_max = 0
        res = 0

        for num in nums:
            res = max(res, prev_max + num)
            prev_max = max(prev_max, num) - 1

        return res


class Solution:
    def maxScoreSightseeingPair(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: brute-force
        """
        res = 0
        
        for right, right_num in enumerate(nums):
            for left in range(right):
                
                left_num = nums[left]
                score = left_num + right_num + left - right
                res = max(res, score)
        
        return res


print(Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11)
print(Solution().maxScoreSightseeingPair([1, 2]) == 2)
