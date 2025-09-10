class Solution:
    def findMaxConsecutiveOnes(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        counter = 0
        max_counter = 0
        last_number = 0
        
        for number in numbers:
            if number:
                if last_number:
                    counter += 1
                else:
                    counter = 1
                    last_number = 1
                max_counter = max(max_counter, counter)
            else:
                counter = 0
                last_number = 0
            
        return max_counter


class Solution:
    def findMaxConsecutiveOnes(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        counter = 0
        max_counter = 0
        
        for number in numbers:
            if number:
                counter += 1
            else:
                max_counter = max(max_counter, counter)
                counter = 0
            
        return max(max_counter, counter)


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3)
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2)
print(Solution().findMaxConsecutiveOnes([1]) == 1)
print(Solution().findMaxConsecutiveOnes([0]) == 0)