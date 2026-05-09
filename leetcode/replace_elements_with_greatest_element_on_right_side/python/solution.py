class Solution:
    def replaceElements(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        res = []
        prev = -1

        for idx in range(len(nums) - 1, -1, -1):
            res.append(prev)
            prev = max(prev, nums[idx])

        res.reverse()
        return res


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1])
print(Solution().replaceElements([400]) == [-1])
