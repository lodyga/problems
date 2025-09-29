
#                      -2     
#                    /    \    
#                  -2+1   1    
#                       /   \ 
#                     1-3    -3
#                     /  \
#                  -2+4   4
#                        /  \
#                      4-1   -1
#                      /  \
#                   3+2    2
#                  /   \
#                5+1    1
# 
# for [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# cummulative sum [-2, 1, -2, 4, 3, 5, 6, 1, 4]


class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: Kadane's Algorithm
        """
        total = 0
        max_sum = numbers[0]

        for number in numbers:
            if total < 0:
                total = 0
            total += number
            max_sum = max(max_sum, total)

        return max_sum


class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        max_sum = numbers[0]
        total = 0
        prev_max = 0
        
        for index in range(len(numbers)):
            total = max(prev_max + numbers[index], numbers[index])
            prev_max = total
            max_sum = max(max_sum, total)
        
        return max_sum


class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        cache = numbers[0]
        largest_sum = numbers[0]

        for number in numbers[1:]:
            cache = max(number, number + cache)
            largest_sum = max(largest_sum, cache)

        return largest_sum


class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        cache = numbers.copy()

        for index in range(1, len(numbers)):
            cache[index] = max(cache[index],
                               cache[index] + cache[index - 1])

        return max(cache)


class Solution:
    def maxSubArray(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up, 
        mutate imput list
        """
        for index in range(1, len(numbers)):
            numbers[index] += max(numbers[index - 1], 0)

        return max(numbers)
    

print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(Solution().maxSubArray([1]) == 1)
print(Solution().maxSubArray([5, 4, -1, 7, 8]) == 23)
print(Solution().maxSubArray([-4, -2, -1, -3]) == -1)