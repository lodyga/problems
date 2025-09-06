class Solution:
    def maxCoins(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n2^n)
        Tags: brute-force
        """
        numbers.insert(0, 1)
        numbers.append(1)

        def dfs(left, right):
            if left > right:
                return 0

            memo = 0
            for index in range(left, right + 1):
                coins = numbers[left - 1] * numbers[index] * numbers[right + 1]
                memo = max(
                    memo,
                    dfs(left, index - 1) + coins + dfs(index + 1, right)
                )

            return memo

        return dfs(1, len(numbers) - 2)


class Solution:
    def maxCoins(self, numbers: list[int]) -> int:
        """
        Time complexity: O(n3)
        Auxiliary space complexity: O(n2)
        Tags: dp, top-down with memoization as array
        """
        numbers.insert(0, 1)
        numbers.append(1)
        memo = [[-1] * len(numbers) for _ in range(len(numbers))]

        def dfs(left, right):
            if left > right:
                return 0
            elif memo[left][right] != -1:
                return memo[left][right]

            for index in range(left, right + 1):
                coins = numbers[left - 1] * numbers[index] * numbers[right + 1]
                memo[left][right] = max(
                    memo[left][right],
                    dfs(left, index - 1) + coins + dfs(index + 1, right)
                )

            return memo[left][right]

        return dfs(1, len(numbers) - 2)


print(Solution().maxCoins([3, 1, 5, 8]) == 167)
print(Solution().maxCoins([1, 5]) == 10)
print(Solution().maxCoins([8, 2, 6, 8, 9, 8, 1, 4, 1, 5, 3, 0, 7, 7, 0, 4, 2]) == 3414)