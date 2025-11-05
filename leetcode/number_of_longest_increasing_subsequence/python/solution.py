class Solution:
    def findNumberOfLIS(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        # [(lis length, lis counter), ]
        cache = [[1, 1] for _ in  range(len(numbers))]

        for index in reversed(range(len(numbers) - 1)):
            lis_length = cache[index][0]
            lis_counter = cache[index][1]
            
            for i2 in range(index + 1, len(numbers)):
                if numbers[index] >= numbers[i2]:
                    continue
                cache_length = cache[i2][0]
                cache_counter = cache[i2][1]
                
                # longer LIS found
                if lis_length < cache_length + 1:
                    lis_length = cache_length + 1
                    lis_counter = cache_counter
                    cache[index] = [lis_length, lis_counter]
                # same length LIS found
                elif lis_length == cache_length + 1:
                    lis_counter += cache_counter
                    cache[index][1] = lis_counter
            
        longest_lis_length = 1
        max_lis_counter = 0
        for lis_length, lis_counter in cache:
            if lis_length > longest_lis_length:
                longest_lis_length = lis_length
                max_lis_counter = lis_counter
            elif lis_length == longest_lis_length:
                max_lis_counter += lis_counter
        
        return max_lis_counter


print(Solution().findNumberOfLIS([1, 3, 5, 4]) == 2)  # [1, 3, 4] and [1, 3, 5]
print(Solution().findNumberOfLIS([1, 3, 5, 4, 7]) == 2)  # [1, 3, 4, 7] and [1, 3, 5, 7]
print(Solution().findNumberOfLIS([2, 2, 2, 2, 2]) == 5)  # [2], [2], [2], [2], [2]
print(Solution().findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]) == 3)  # [1, 2, 3, 4, 7], [1, 2, 3, 5, 7], [1, 2, 4, 5, 7]
print(Solution().findNumberOfLIS([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 27)