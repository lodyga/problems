class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: sorting, counting sort
        """
        res = 0
        min_num = min(nums)
        num_freq = {}
        index = 0

        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        while index < len(nums):
            if min_num in num_freq:
                extras = num_freq[min_num] - 1
                next_num_freq = num_freq.get(min_num + 1, 0) + extras

                if next_num_freq:
                    num_freq[min_num + 1] = next_num_freq

                res += extras
                index += 1

            min_num += 1

        return res


class Solution2:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Tags:
            A: sorting, two pointers
        """
        nums.sort()
        res = 0

        for index in range(len(nums) - 1):
            next_num = nums[index + 1]
            num = nums[index]

            if num < next_num:
                continue

            nums[index + 1] = nums[index] + 1
            res += nums[index + 1] - next_num

        return res


print(Solution().minIncrementForUnique([1, 2, 2]) == 1)
print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]) == 6)
print(Solution().minIncrementForUnique([2, 2, 2, 1]) == 3)
print(Solution().minIncrementForUnique([1, 3, 0, 3, 0]) == 3)
print(Solution().minIncrementForUnique([13, 4, 12, 5, 3, 16, 11, 6, 11, 0, 2, 7, 19, 10, 1, 15, 15, 15, 11, 13]) == 25)
