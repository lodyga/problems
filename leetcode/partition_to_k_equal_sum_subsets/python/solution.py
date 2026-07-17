class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        """
        Time complexity: O(k^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: backtracking with pruning, sorting
        """
        N = len(nums)
        TOTAL = sum(nums)
        if TOTAL % k:
            return False
        UPPER_BOUND = TOTAL // k
        nums.sort(reverse=True)
        subset_sum = [0] * k

        def backtrack(idx):
            if idx == N:
                return True
            
            num = nums[idx]

            for part_idx in range(k):
                if subset_sum[part_idx] + num <= UPPER_BOUND:
                    subset_sum[part_idx] += num
                    if backtrack(idx + 1):
                        return True
                    subset_sum[part_idx] -= num

                # pruning
                if subset_sum[part_idx] == 0:
                    break
            return False

        return backtrack(0)


print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) == True)
print(Solution().canPartitionKSubsets([1, 2, 3, 4], 3) == False)
print(Solution().canPartitionKSubsets([3, 9, 4, 5, 8, 8, 7, 9, 3, 6, 2, 10, 10, 4, 10, 2], 10) == False)
print(Solution().canPartitionKSubsets([4, 5, 9, 3, 10, 2, 10, 7, 10, 8, 5, 9, 4, 6, 4, 9], 5) == True)
print(Solution().canPartitionKSubsets([10, 1, 10, 9, 6, 1, 9, 5, 9, 10, 7, 8, 5, 2, 10, 8], 11) == False)


class Solution:
    def canPartitionKSubsets(self, numbers: list[int], k: int) -> bool:
        """
        Time complexity: O(k2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: backtracking with pruning, sorting
        """
        TOTAL = sum(numbers)
        if TOTAL % k:
            return False
        target = TOTAL // k
        numbers.sort(reverse=True)
        used = [False] * len(numbers)  # idx is used

        def dfs(idx, k, SUBSET_SUM):
            if SUBSET_SUM == target:
                return dfs(0, k - 1, 0)
            elif k == 0:
                return True

            for i in range(idx, len(numbers)):
                if used[i] or SUBSET_SUM + numbers[i] > target:
                    continue
                used[i] = True
                if dfs(i + 1, k, SUBSET_SUM + numbers[i]):
                    return True
                used[i] = False

                if SUBSET_SUM == 0: # Pruning
                    return False

            return False

        return dfs(0, k, 0)