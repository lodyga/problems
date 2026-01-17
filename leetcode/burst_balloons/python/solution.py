class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n2^n)
        Tags:
            A: brute-force
        """
        nums.insert(0, 1)
        nums.append(1)

        def dfs(left, right):
            if left > right:
                return 0

            res = 0
            for index in range(left, right + 1):
                coins = nums[left - 1] * nums[index] * nums[right + 1]
                res = max(
                    res, 
                    dfs(left, index - 1) + coins + dfs(index + 1, right)
                )
            
            return res

        return dfs(1, len(nums) - 2)


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags:
            DS: array
            A: top-down
        """
        nums.insert(0, 1)
        nums.append(1)
        # [(left, right): max coins for current range]
        memo = [[-1] * len(nums) for _ in range(len(nums))]

        def dfs(left, right):
            if left > right:
                return 0
            elif memo[left][right] != -1:
                return memo[left][right]

            res = 0
            for index in range(left, right + 1):
                # number[index] is popped last not first
                coins = nums[left - 1] * nums[index] * nums[right + 1]
                res = max(
                    res, 
                    dfs(left, index - 1) + coins + dfs(index + 1, right)
                )
            
            memo[left][right] = res
            return res

        return dfs(1, len(nums) - 2)


print(Solution().maxCoins([1, 5]) == 10)
print(Solution().maxCoins([3, 1, 5, 8]) == 167)
print(Solution().maxCoins([8, 2, 6, 8, 9, 8, 1, 4, 1, 5, 3, 0, 7, 7, 0, 4, 2]) == 3414)
print(Solution().maxCoins([18, 2, 8, 47, 99, 80, 12, 75, 97, 3, 46, 75, 71, 99, 55, 54, 39, 55, 73, 21, 67, 35, 89, 60, 95, 45, 89, 96, 61, 70, 30, 34, 80, 7, 42, 10, 8, 72, 9, 84, 9, 49, 11, 47, 87, 84, 76, 87, 40, 98, 25, 10, 6, 13, 94, 43, 34, 72, 79, 52, 75, 91, 45, 45, 90, 36, 9, 61, 58, 80, 13, 18, 67, 17, 4, 92, 71, 7, 44, 72, 45, 41, 72, 72, 94, 20, 21, 42, 15, 45, 35, 5, 6, 25, 17, 87, 98, 75, 27, 74, 11, 48, 87, 50, 58, 9, 36, 90, 33, 35, 94, 72, 84, 1, 21, 4, 75, 80, 28, 48, 57, 40, 87, 69, 89, 93, 28, 100, 44, 52, 87, 17, 15, 65, 67, 72, 5, 92, 43, 90, 99, 53, 99, 55, 44, 22, 78, 93, 30, 72, 0, 28, 42, 83, 99, 1, 75, 2, 61, 1, 25, 73, 78, 86, 20, 75, 15, 53, 44, 51, 9, 3, 85, 56, 83, 22, 18, 5, 73, 10, 53, 56, 29, 87, 76, 74, 12, 83, 33, 68, 20, 51, 69, 31, 92, 24, 25, 51, 94, 26, 34, 25, 4, 56, 19, 56, 0, 58, 22, 94, 53, 78, 38, 20, 29, 74, 46, 21, 44, 16, 77, 3, 49, 79, 28, 83, 61, 13, 39, 12, 91, 50, 60, 92, 100, 2, 5, 52, 98, 3, 80, 11, 34, 60, 35, 1, 30, 91, 51, 52, 39, 72, 4, 29, 86, 64, 39, 51, 74, 99, 99, 32, 12, 16, 61, 88, 5, 82, 85, 19, 45, 80, 45, 5, 63, 23, 51, 91, 97, 24, 35, 42, 60, 100, 8, 31, 39, 54, 80, 66, 28, 52, 75, 25, 66, 51, 20, 98, 99, 78]) == 111830214)
