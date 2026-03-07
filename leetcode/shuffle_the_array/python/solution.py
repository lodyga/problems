class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: iteration
        """
        res = []

        for index in range(n):
            res.append(nums[index])
            res.append(nums[index + n])

        return res


print(Solution().shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7])
print(Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1])
print(Solution().shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2])
