class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: array
            A: two pointers, in-place method
        """
        index1 = m - 1
        index2 = n - 1
        index = m + n - 1

        while index1 > -1 or index2 > -1:
            num1 = nums1[index1] if index1 > -1 else nums2[0] - 1
            num2 = nums2[index2] if index2 > -1 else nums1[0] - 1

            if num1 > num2:
                nums1[index] = num1
                index1 -= 1
            else:
                nums1[index] = num2
                index2 -= 1
            index -= 1

        return nums1


print(Solution().merge([1], 1, [], 0) == [1])
print(Solution().merge([0], 0, [1], 1) == [1])
print(Solution().merge([2, 0], 1, [1], 1) == [1, 2])
print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6])
print(Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3) == [-1, 0, 0, 1, 2, 2, 3, 3, 3])
print(Solution().merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3) == [1, 2, 3, 4, 5, 6])
