class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash set
            A: iteration
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: One-liner
        """
        return len(nums) != len(set(nums))


print(Solution().containsDuplicate([1, 2, 3]) == False)
print(Solution().containsDuplicate([1, 2, 3, 4]) == False)
print(Solution().containsDuplicate([1, 2, 3, 1]) == True)
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)
