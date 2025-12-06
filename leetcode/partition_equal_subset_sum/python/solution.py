class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n2)
            O(n*s)
            n: nums length
            s: nums sum
        Auxiliary space complexity: O(n)
            O(s)
        Tags: 
            DS: bottom-up, hash set
            A: bottom-up
        """
        total = sum(nums)
        if total % 2:
            return False
        half = total >> 1
        num_set = set()

        for num in nums:
            num_set_update = {set_num + num for set_num in num_set}
            num_set_update.add(num)
            # num_set |= num_set_update
            num_set.update(num_set_update)
            if half in num_set:
                return True

        return False


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        Time complexity: O(2^n)
            n: nums length
        Auxiliary space complexity: O(n)
        Tags: 
            A: brute-force, pure recursion
        """
        total = sum(nums)
        if total % 2:
            return False
        half = total >> 1

        def dfs(index: int, subset_sum: int) -> bool:
            if subset_sum >= half:
                return subset_sum == half
            elif index == len(nums):
                return False

            num = nums[index]
            # skip
            skip = dfs(index + 1, subset_sum)
            # take
            take = dfs(index + 1, subset_sum + num)

            can_partition = skip or take
            return can_partition

        return dfs(0, 0)


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n2)
            O(n*s)
            n: nums length
            s: nums sum
        Auxiliary space complexity: O(n*s)
        Tags: 
            DS: hash map
            A: top-down
        """
        total = sum(nums)
        if total % 2:
            return False
        half = total >> 1
        # {(index, subset sum): can partition: bool}
        memo = {}

        def dfs(index: int, subset_sum: int) -> bool:
            if subset_sum >= half:
                return subset_sum == half
            elif index == len(nums):
                return False
            elif (index, subset_sum) in memo:
                return memo[(index, subset_sum)]

            num = nums[index]
            # skip
            skip = dfs(index + 1, subset_sum)
            # take
            take = dfs(index + 1, subset_sum + num) if skip is False else skip

            can_partition = skip or take
            memo[(index, subset_sum)] = can_partition
            return can_partition

        return dfs(0, 0)


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        Time complexity: O(2^n)
            n: nums length
        Auxiliary space complexity: O(n)
        Tags: 
            A: brute-force, backtracking
        """
        total = sum(nums)
        if total % 2:
            return False
        half = total >> 1
        subset = []

        def dfs(index: int) -> bool:
            if sum(subset) == half:
                return True
            elif (
                index == len(nums) or
                sum(subset) > half
            ):
                return False

            subset.append(nums[index])
            if dfs(index + 1):
                return True
            subset.pop()
            if dfs(index + 1):
                return True

            return False

        return dfs(0)


print(Solution().canPartition([2]) == False)
print(Solution().canPartition([2, 2]) == True)
print(Solution().canPartition([1, 5, 11, 5]) == True)
print(Solution().canPartition([14, 9, 8, 4, 3, 2]) == True)
print(Solution().canPartition([1, 2, 5]) == False)
print(Solution().canPartition([3, 3, 3, 4, 5]) == True)
print(Solution().canPartition([1, 2, 3, 5]) == False)
print(Solution().canPartition([1]) == False)
print(Solution().canPartition([2, 2, 1, 1]) == True)
print(Solution().canPartition([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 99, 97]) == False)
