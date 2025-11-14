class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: greedy
        """
        min_number = arrays[0][0]
        max_number = arrays[0][-1]
        max_distance = 0

        for index in range(1, len(arrays)):
            current_min = arrays[index][0]
            current_max = arrays[index][-1]
            max_distance = max(
                max_distance,
                current_max - min_number,
                max_number - current_min
            )
            min_number = min(min_number, current_min)
            max_number = max(max_number, current_max)

        return max_distance


print(Solution().maxDistance([[1, 2, 3], [4, 5], [1, 2, 3]]) == 4)
print(Solution().maxDistance([[1], [1]]) == 0)
