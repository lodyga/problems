class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: in-place, negative marking
        """
        res = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                res.append(abs(num))
            else:
                nums[index] *= -1

        return res


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: in-place, upper bound marking
        """
        UPPER_BOUND = len(nums) + 1
        res = []

        for num in nums:
            index = (num % UPPER_BOUND) - 1

            if nums[index] > UPPER_BOUND:
                res.append(num % UPPER_BOUND)
            else:
                nums[index] += UPPER_BOUND

        return res


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
        """
        res = []
        num_set = set()
        
        for num in nums:
            if num in num_set:
                res.append(num)
            else:
                num_set.add(num)
        
        return res


print(sorted(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) , sorted([2, 3]))
print(sorted(Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) == sorted([2, 3]))
print(sorted(Solution().findDuplicates([1, 1, 2])) == sorted([1]))
print(sorted(Solution().findDuplicates([1])) == sorted([]))
print(sorted(Solution().findDuplicates([10, 2, 5, 10, 9, 1, 1, 4, 3, 7])) == sorted([10, 1]))
