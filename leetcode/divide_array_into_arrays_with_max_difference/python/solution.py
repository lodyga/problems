class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting
        """
        nums.sort()

        for index in range(0, len(nums), 3):
            if nums[index + 2] - nums[index] > k:
                return []

        return [nums[index: index + 3]
                for index in range(0, len(nums), 3)]


class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting
        """
        nums.sort()
        res = []

        for index in range(0, len(nums), 3):
            if nums[index + 2] - nums[index] > k:
                return []
            else:
                res.append(nums[index: index + 3])

        return res


print(Solution().divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2) == [[1, 1, 3], [3, 4, 5], [7, 8, 9]])
print(Solution().divideArray([2, 4, 2, 2, 5, 2], 2) == [])
print(Solution().divideArray([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14) == [[2, 2, 2], [4, 5, 5], [5, 5, 7], [7, 8, 8], [9, 9, 10], [11, 12, 12]])
