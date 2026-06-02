class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: negative marking, in-place method
        """
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])

        return [idx + 1
                for idx, num in enumerate(nums)
                if num > 0
                ]


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set, list
            A: negative marking, in-place method
        """
        res = set(range(1, len(nums) + 1))

        for num in nums:
            res.discard(num)

        return list(res)


print(Solution().findDisappearedNumbers([1, 1]) == [2])
print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6])
