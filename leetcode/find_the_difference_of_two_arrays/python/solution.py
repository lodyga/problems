class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: iteration
        """
        num1_set = set(nums1)
        num2_set = set(nums2)

        distinct_a = list(num1_set - num2_set)
        distinct_b = list(num2_set - num1_set)

        return [distinct_a, distinct_b]


print(Solution().findDifference([1, 2, 3],  [2, 4, 6]) == [[1, 3], [4, 6]])
print(Solution().findDifference([1, 2, 3, 3],  [1, 1, 2, 2]) == [[3], []])
