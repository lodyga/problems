class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting
        """
        diff_counter = 0
        sorted_heights = sorted(heights)

        for index in range(len(heights)):
            if heights[index] != sorted_heights[index]:
                diff_counter += 1

        return diff_counter


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: counting sort
        """
        height_bucket = [0] * 100
        for height in heights:
            height_bucket[height - 1] += 1
        
        sorted_heights = []
        for height, count in enumerate(height_bucket):
            for _ in range(count):
                sorted_heights.append(height + 1)
        
        diff_counter = 0
        for index in range(len(heights)):
            if heights[index] != sorted_heights[index]:
                diff_counter += 1

        return diff_counter


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]) == 3)
print(Solution().heightChecker([5, 1, 2, 3, 4]) == 5)
print(Solution().heightChecker([1, 2, 3, 4, 5]) == 0)
