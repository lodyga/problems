class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags: sorting
        """
        sorted_heights = sorted(heights)

        return sum(
            True
            for index in range(len(heights))
            if heights[index] != sorted_heights[index]
        )


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: counting sort
        """
        height_bucket = [0] * 101
        for height in heights:
            height_bucket[height] += 1
        
        sorted_heights = []
        for index in range(len(height_bucket)):
            if height_bucket[index] == 0:
                continue
            for _ in range(height_bucket[index]):
                sorted_heights.append(index)
        
        return sum(
            True
            for index in range(len(heights))
            if heights[index] != sorted_heights[index]
        )


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]) == 3)
print(Solution().heightChecker([5, 1, 2, 3, 4]) == 5)
print(Solution().heightChecker([1, 2, 3, 4, 5]) == 0)