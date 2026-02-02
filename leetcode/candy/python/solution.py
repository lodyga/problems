class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: greedy
        """
        N = len(ratings)
        candies = [1] * N

        for index in range(N - 1):
            if ratings[index] < ratings[index + 1]:
                candies[index + 1] = candies[index] + 1

        for index in range(N - 2, -1, -1):
            if (
                ratings[index] > ratings[index + 1] and 
                candies[index] < candies[index + 1] + 1
            ):
                candies[index] = candies[index + 1] + 1

        return sum(candies)


print(Solution().candy([1, 0, 2]) == 5)
print(Solution().candy([1, 2, 2]) == 4)
print(Solution().candy([1, 2, 3, 4]) == 10)
print(Solution().candy([4, 3, 2, 1]) == 10)
print(Solution().candy([1, 3, 4, 5, 2]) == 11)
