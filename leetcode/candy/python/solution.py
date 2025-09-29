class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: greedy
        """
        candy_length = len(ratings)
        candies = [1] * candy_length

        for index in range(candy_length - 1):
            if ratings[index] < ratings[index + 1]:
                candies[index + 1] = candies[index] + 1
        
        total_candies = candies[-1]
        for index in reversed(range(candy_length - 1)):
            if ratings[index] > ratings[index + 1]:
                candies[index] = max(candies[index], candies[index + 1] + 1)
            total_candies += candies[index]
        
        return total_candies


print(Solution().candy([1, 0, 2]) == 5)
print(Solution().candy([1, 2, 2]) == 4)
print(Solution().candy([1, 2, 3, 4]) == 10)
print(Solution().candy([4, 3, 2, 1]) == 10)