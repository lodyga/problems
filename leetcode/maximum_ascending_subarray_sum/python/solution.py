class Solution:
    def maxAscendingSum(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        prev_number = 0
        window = 0
        max_window = 0
        
        for number in numbers:
            if number > prev_number:
                window += number
                max_window = max(max_window, window)
            else:
                window = number
            prev_number = number

        return max_window


print(Solution().maxAscendingSum([10, 20, 30, 5, 10, 50]) == 65)
print(Solution().maxAscendingSum([10, 20, 30, 40, 50]) == 150)
print(Solution().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) == 33)