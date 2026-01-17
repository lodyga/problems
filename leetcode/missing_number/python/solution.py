class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        xor = 0

        for num in range(len(nums) + 1):
            xor ^= num

        for num in nums:
            xor ^= num

        return xor


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: iteration
        """
        number_set = set(nums)
        for number in range(len(nums) + 1):
            if number not in number_set:
                return number


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: math
        """
        num_sum = sum(nums)
        range_sum = sum(range(len(nums) + 1))
        return range_sum - num_sum


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: math
        """
        num_sum = sum(nums)
        range_sum = len(nums) * (len(nums) + 1) // 2
        return range_sum - num_sum


print(Solution().missingNumber([3, 0, 1]) == 2)
print(Solution().missingNumber([0, 1]) == 2)
print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8)
