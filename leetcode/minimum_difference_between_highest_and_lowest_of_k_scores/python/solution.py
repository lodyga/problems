class Solution:
    def minimumDifference(self, numbers: list[int], k: int) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        """
        if k == 1:
            return 0

        numbers.sort()
        min_diff = float("inf")

        for index in range(len(numbers) - k + 1):
            min_diff = min(min_diff, numbers[index + k - 1] - numbers[index])

        return min_diff


class Solution:
    def minimumDifference(self, numbers: list[int], k: int) -> int:
        numbers.sort()
        return min(numbers[index + k - 1] - numbers[index]
                   for index in range(len(numbers) - k + 1))


print(Solution().minimumDifference([90], 1), 0)
print(Solution().minimumDifference([9, 4, 1, 7], 2), 2)
print(Solution().minimumDifference([87063, 61094, 44530, 21297, 95857, 93551, 9918], 6), 74560)
