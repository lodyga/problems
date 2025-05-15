"""
draft
                  .
            /           \
           1            .
         /    \       /    \
        5     .       5     .
       /\     /\     /\    /\
      11 .   11 .   11 .  11 .
    /\
   5 .
"""


class Solution:
    def canPartition(self, numbers: list[int]) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up
        """
        total = sum(numbers)
        if total % 2:
            return False
        half = total // 2
        # set with addition neutral element
        subset = set({0})

        for number in numbers:
            subset_copy = subset.copy()
            subset = {val + number for val in subset}
            subset.update(subset_copy)

            if half in subset:
                return True

        return False


class Solution:
    def canPartition(self, numbers: list[int]) -> bool:
        """
        O(n2), O(n)
        dp, top-down with memoization as hash map
        """
        total = sum(numbers)
        if total % 2:  # if odd sum (cannot be split in half)
            return False

        memo = {}  # {(index, target): bool}
        
        def dfs(index: int, target: int) -> bool:
            if (index, target) in memo:
                return memo[(index, target)]
            elif target <= 0:
                return target == 0
            elif index == len(numbers):
                return False

            memo[(index, target)] = (dfs(index + 1, target - numbers[index]) or 
                                     dfs(index + 1, target))
            return memo[(index, target)]

        return dfs(0, total // 2)


class Solution:
    def canPartition(self, numbers: list[int]) -> bool:
        """
        O(2^n), O(n)
        brute force, pure recursion, tle
        converts to top-down
        """
        total = sum(numbers)
        if total % 2:  # if odd sum (cannot be split in half)
            return False

        def dfs(index: int, target: int) -> bool:
            if target <= 0:
                return target == 0
            elif index == len(numbers):
                return False
        
            return (dfs(index + 1, target - numbers[index]) or
                    dfs(index + 1, target))

        return dfs(0, total // 2)


class Solution:
    def canPartition(self, numbers: list[int]) -> bool:
        """
        O(2^n), O(n)
        brute force, backtracking, tle
        """
        total = sum(numbers)
        if total % 2:
            return False
        half = total // 2
        subset = []

        def dfs(index: int) -> bool:
            if sum(subset) == half:
                return True
            elif (index == len(numbers) or
                  sum(subset) > half):
                return

            subset.append(numbers[index])
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