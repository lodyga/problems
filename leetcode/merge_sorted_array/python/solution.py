class Solution:
    def merge(self, numbes_1: list[int], m: int, numbes_2: list[int], n: int) -> None:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers, in-place method
        """
        right_1 = m - 1
        right_2 = n - 1
        index = m + n - 1

        while right_1 != -1 and right_2 != -1:
            if numbes_1[right_1] > numbes_2[right_2]:
                numbes_1[index] = numbes_1[right_1]
                right_1 -= 1
            else:
                numbes_1[index] = numbes_2[right_2]
                right_2 -= 1
            index -= 1
        
        while right_2 != -1:
            numbes_1[index] = numbes_2[right_2]
            right_2 -= 1
            index -= 1

        return numbes_1


print(Solution().merge([1], 1, [], 0) == [1])
print(Solution().merge([0], 0, [1], 1) == [1])
print(Solution().merge([2, 0], 1, [1], 1) == [1, 2])
print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6])
print(Solution().merge([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3) == [-1, 0, 0, 1, 2, 2, 3, 3, 3])
print(Solution().merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3) == [1, 2, 3, 4, 5, 6])