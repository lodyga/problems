class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        Time complexity: O(n*m)
            n: stone count
            m: stone sum
        Auxiliary space complexity: O(n*m)
        Tags:
            DS: hash map
            A: top-down
        """
        stone_sum = sum(stones)
        half = stone_sum // 2
        memo = {}

        def dfs(index: int, total: int) -> int:
            if (
                total >= half or 
                index == len(stones)
            ):
                # Returns the difference between both part sums.
                return abs(total - (stone_sum - total))
            elif (index, total) in memo:
                return memo[(index, total)]

            stone = stones[index]
            skip = dfs(index + 1, total)
            take = dfs(index + 1, stone + total)
            res = min(skip, take)
            memo[(index, total)] = res
            return res

        return dfs(0, 0)


print(Solution().lastStoneWeightII([3, 3]) == 0)
print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]) == 1)
print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]) == 5)
