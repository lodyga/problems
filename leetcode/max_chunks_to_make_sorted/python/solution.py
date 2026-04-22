class Solution:
    def maxChunksToSorted(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: greedy
        """
        max_num = 0
        counter = 0

        for index, num in enumerate(nums):
            max_num = max(max_num, num)

            if max_num == index:
                counter += 1

        return counter


print(Solution().maxChunksToSorted([4, 3, 2, 1, 0]) == 1)
print(Solution().maxChunksToSorted([1, 0, 2, 3, 4]) == 4)
print(Solution().maxChunksToSorted([0]) == 1)
