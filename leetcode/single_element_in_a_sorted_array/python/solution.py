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
            middle = (left + right) >> 1

            if (
                left == right or
                nums[middle - 1] != nums[middle] != nums[middle + 1]
            ):
                return nums[middle]

            if nums[middle] == nums[middle + 1]:
                if (middle - left) % 2 == 1:
                    right = middle - 1
                else:
                    left = middle + 2

            elif nums[middle - 1] == nums[middle]:
                if (middle - left) % 2 == 1:
                    left = middle + 1
                else:
                    right = middle - 2


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


print(Solution().singleNonDuplicate([1]) == 1)
print(Solution().singleNonDuplicate([1, 2, 2]) == 1)
print(Solution().singleNonDuplicate([1, 1, 2]) == 2)
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3]) == 2)
print(Solution().singleNonDuplicate([1, 1, 2, 2, 3, 4, 4]) == 3)
print(Solution().singleNonDuplicate([2, 2, 3, 3, 4]) == 4)
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4]) == 2)
print(Solution().singleNonDuplicate([1, 1, 3, 3, 4, 4, 5]) == 5)
print(Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10)
print(Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2)
print(Solution().singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)
