class Solution:
    def mergeArrays(self, numbers1: list[list[int]], numbers2: list[list[int]]) -> list[list[int]]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pionters
        """
        index1 = 0
        index2 = 0
        merged_arrays = []

        while (
            index1 < len(numbers1) or 
            index2 < len(numbers2)
        ):
            if index1 == len(numbers1):
                merged_arrays.append(numbers2[index2])
                index2 += 1
            elif index2 == len(numbers2):
                merged_arrays.append(numbers1[index1])
                index1 += 1
            elif numbers1[index1][0] < numbers2[index2][0]:
                merged_arrays.append(numbers1[index1])
                index1 += 1
            elif numbers2[index2][0] < numbers1[index1][0]:
                merged_arrays.append(numbers2[index2])
                index2 += 1
            else:
                merged_arrays.append([numbers1[index1][0], numbers1[index1][1] + numbers2[index2][1]])
                index1 += 1
                index2 += 1
        return merged_arrays


print(Solution().mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]) == [[1, 6], [2, 3], [3, 2], [4, 6]])
print(Solution().mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]])