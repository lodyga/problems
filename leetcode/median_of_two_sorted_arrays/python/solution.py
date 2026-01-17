r"""
draft
1, 2, 3 | 4, 5
1, 2, 3 | 4, 5, 6, 7, 8
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # O(n)
        num_len = len(nums1) + len(nums2)
        is_odd = num_len % 2
        nums = []

        index1 = index2 = 0
        while index1 < len(nums1) or index2 < len(nums2):
            num1 = nums1[index1] if index1 < len(nums1) else 10**6 + 1
            num2 = nums2[index2] if index2 < len(nums2) else 10**6 + 1
            if num1 < num2:
                nums.append(num1)
                index1 += 1
            else:
                nums.append(num2)
                index2 += 1
        
        if is_odd:
            return nums[num_len // 2]
        else:
            return (nums[num_len // 2 - 1] + nums[num_len // 2]) / 2
            

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Time complexity: O(log(min(n+m)))
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        a = nums1
        b = nums2
        if len(b) < len(a):
            a, b = b, a
        
        length = len(a) + len(b)
        half = length // 2
        left = 0
        right = len(a) - 1

        while True:
            mid_a = (left + right) // 2
            mid_b = half - mid_a - 2

            a_left = a[mid_a] if mid_a >= 0 else -10**6 - 1
            a_right = a[mid_a + 1] if mid_a + 1 < len(a) else 10**6 + 1
            b_left = b[mid_b] if mid_b >= 0 else -10**6 - 1
            b_right = b[mid_b + 1] if mid_b + 1 < len(b) else 10**6 + 1
            
            if a_left <= b_right and b_left <= a_right:
                if length % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                right = mid_a - 1
            else:
                left = mid_a + 1


print(Solution().findMedianSortedArrays([1, 3], [2]) == 2)
print(Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5)
print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5]) , 4)
print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5]) == 4)
print(Solution().findMedianSortedArrays([], [5]) == 5)
print(Solution().findMedianSortedArrays([5], []) == 5)
