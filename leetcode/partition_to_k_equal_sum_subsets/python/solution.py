class Solution:
    def canPartitionKSubsets(self, numbers: list[int], k: int) -> bool:
        """
        Time complexity: O(2^n)
            O(k^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking with pruning
        """
        total = sum(numbers)
        if total % k:
            return False
        target = total // k
        numbers.sort(reverse=True)
        parts_values = [target] * k

        def dfs(index):
            if index == len(numbers):
                return True

            for part_index in range(k):
                if parts_values[part_index] - numbers[index] >= 0:
                    parts_values[part_index] -= numbers[index]
                    if dfs(index + 1):
                        return True
                    parts_values[part_index] += numbers[index]

                if (
                    parts_values[part_index] == target or
                    parts_values[part_index] == numbers[index]
                ):
                    break

            return False
        return dfs(0)


class Solution:
    def canPartitionKSubsets(self, numbers: list[int], k: int) -> bool:
        """
        Time complexity: O(k2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        total = sum(numbers)
        if total % k:
            return False
        target = total // k
        numbers.sort(reverse=True)
        used = [False] * len(numbers)  # index is used

        def dfs(index, k, subset_sum):
            if subset_sum == target:
                return dfs(0, k - 1, 0)
            elif k == 0:
                return True

            for i in range(index, len(numbers)):
                if used[i] or subset_sum + numbers[i] > target:
                    continue
                used[i] = True
                if dfs(i + 1, k, subset_sum + numbers[i]):
                    return True
                used[i] = False

                if subset_sum == 0: # Pruning
                    return False

            return False

        return dfs(0, k, 0)


print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) == True)
print(Solution().canPartitionKSubsets([1, 2, 3, 4], 3) == False)
print(Solution().canPartitionKSubsets([3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10) == False)
print(Solution().canPartitionKSubsets([4, 5, 9, 3, 10, 2, 10, 7, 10, 8, 5, 9, 4, 6, 4, 9], 5) == True)
print(Solution().canPartitionKSubsets([10, 1, 10, 9, 6, 1, 9, 5, 9, 10, 7, 8, 5, 2, 10, 8], 11) == False)


# wrong solution
class Solution:
    def canPartitionKSubsets(self, numbers: list[int], k: int) -> bool:
        """
        Time complexity: O(k2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking
        """
        total = sum(numbers)
        if total % k:
            return False
        target = total // k
        numbers.sort(reverse=True)
        used = [False] * len(numbers)  # index is used

        def dfs(index, current_part_value):
            if current_part_value == target:
                return True
            elif current_part_value > target:
                return False
            elif index == len(numbers):
                return False

            elif not used[index]:
                used[index] = True
                if dfs(index + 1, current_part_value + numbers[index]):
                    return True
                used[index] = False

            return dfs(index + 1, current_part_value)

        return all(dfs(0, 0) for _ in range(k))


