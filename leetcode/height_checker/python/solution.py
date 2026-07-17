class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting
        """
        sorted_heights = sorted(heights)
        res = 0

        for height, s_height in zip(heights, sorted_heights):
            if height != s_height:
                res += 1

        return res


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: counting sort
        """
        height_freq = [0] * 100
        res = 0
        idx = 0

        for height in heights:
            height_freq[height - 1] += 1

        for height, freq in enumerate(height_freq, 1):
            if freq:
                for _ in range(freq):
                    if height != heights[idx]:
                        res += 1

                    idx += 1

        return res


print(Solution().heightChecker([1, 1, 4, 2, 1, 3]) == 3)
print(Solution().heightChecker([5, 1, 2, 3, 4]) == 5)
print(Solution().heightChecker([1, 2, 3, 4, 5]) == 0)
print(Solution().heightChecker([10, 6, 6, 10, 10, 9, 8, 8, 3, 3, 8, 2, 1, 5, 1, 9, 5, 2, 7, 4, 7, 7]) == 22)
