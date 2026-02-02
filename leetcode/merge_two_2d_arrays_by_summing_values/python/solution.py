class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n + m)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: two pionters
        """
        index1 = 0
        index2 = 0
        res = []

        while index1 < len(nums1) and index2 < len(nums2):
            key1, val1 = nums1[index1]
            key2, val2 = nums2[index2]

            if key1 == key2:
                res.append([key1, val1 + val2])
                index1 += 1
                index2 += 1
            elif key1 < key2:
                res.append([key1, val1])
                index1 += 1
            else:
                res.append([key2, val2])
                index2 += 1

        while index1 < len(nums1):
            res.append(nums1[index1])
            index1 += 1

        while index2 < len(nums2):
            res.append(nums2[index2])
            index2 += 1

        return res


class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n + m)
        Auxiliary space complexity: O(1)
        Tags:
            DS: list
            A: two pionters
        """
        index1 = 0
        index2 = 0
        res = []

        while index1 < len(nums1) or index2 < len(nums2):
            if index1 == len(nums1):
                res.append(nums2[index2])
                index2 += 1
                continue
            elif index2 == len(nums2):
                res.append(nums1[index1])
                index1 += 1
                continue

            key1, val1 = nums1[index1]
            key2, val2 = nums2[index2]

            if key1 == key2:
                res.append([key1, val1 + val2])
                index1 += 1
                index2 += 1
            elif key1 < key2:
                res.append([key1, val1])
                index1 += 1
            else:
                res.append([key2, val2])
                index2 += 1

        return res


print(Solution().mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]) == [[1, 6], [2, 3], [3, 2], [4, 6]])
print(Solution().mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]])
