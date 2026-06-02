class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        Time complexity: O(logn)
        Auxiliary space complexity: O(1)
        Tags:
            A: binary search
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_num = nums[mid]

            if left == right:
                return mid_num

            elif mid_num == nums[mid + 1]:
                if (right - mid) % 2 == 0:
                    left = mid + 2
                else:
                    right = mid - 1

            elif mid_num == nums[mid - 1]:
                if (mid - left) % 2 == 0:
                    right = mid - 2
                else:
                    left = mid + 1

            else:
                return mid_num


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        xor = 0

        for num in nums:
            xor ^= num

        return xor


print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2)
print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10)
print(Solution().singleNonDuplicate([1]) == 1)
print(Solution().singleNonDuplicate([1, 2, 2]) == 1)
print(Solution().singleNonDuplicate([1, 1, 2]) == 2)
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3]) == 2)
print(Solution().singleNonDuplicate([1, 1, 2, 2, 3, 4, 4]) == 3)
print(Solution().singleNonDuplicate([2, 2, 3, 3, 4]) == 4)
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4]) == 2)
print(Solution().singleNonDuplicate([1, 1, 3, 3, 4, 4, 5]) == 5)
print(Solution().singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)
