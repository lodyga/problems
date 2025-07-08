r"""
draft
1, 2, 3 | 4, 5
1, 2, 3 | 4, 5, 6, 7, 8
"""


class Solution:
    def findMedianSortedArrays(self, numbers1: list[int], numbers2: list[int]) -> float:
        """
        Time complexity: O(log(min(n+m)))
        Auxiliary space complexity: O(1)
        Tags: binary search
        """
        a = numbers1
        b = numbers2
        if len(b) < len(a):
            a, b = b, a
        
        length = len(a) + len(b)
        half = length // 2
        left = 0
        right = len(a) - 1

        while True:
            middle_a = (left + right) // 2
            middle_b = half - middle_a - 2

            a_left = a[middle_a] if middle_a >= 0 else float("-inf")
            a_right = a[middle_a + 1] if middle_a + 1 < len(a) else float("inf")
            b_left = b[middle_b] if middle_b >= 0 else float("-inf")
            b_right = b[middle_b + 1] if middle_b + 1 < len(b) else float("inf")
            
            if a_left <= b_right and b_left <= a_right:
                if length % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                right = middle_a - 1
            else:
                left = middle_a + 1


print(Solution().findMedianSortedArrays([1, 3], [2]) == 2)
print(Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5]) == 4)
print(Solution().findMedianSortedArrays([], [5]) == 5)
print(Solution().findMedianSortedArrays([5], []) == 5)