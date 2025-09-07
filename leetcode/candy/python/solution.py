class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: greedy
        """
        candy_length = len(ratings)
        candy_list = [1] * candy_length
        candy_sum = 0

        for index in range(candy_length - 1):
            if ratings[index] < ratings[index + 1]:
                candy_list[index + 1] = candy_list[index] + 1
        
        for index in reversed(range(candy_length - 1)):
            if ratings[index] > ratings[index + 1]:
                candy_list[index] = max(candy_list[index], candy_list[index + 1] + 1)
            candy_sum += candy_list[index]
        
        return candy_sum + candy_list[-1]


print(Solution().candy([1, 0, 2]) == 5)
print(Solution().candy([1, 2, 2]) == 4)
print(Solution().candy([1, 2, 3, 4]) == 10)
print(Solution().candy([4, 3, 2, 1]) == 10)