class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        """
        Time complexity: O(4^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking with pruning
        """
        perimeter = sum(matchsticks)
        if perimeter % 4:
            return False
        side_length = perimeter // 4
        sides = [side_length] * 4
        matchsticks.sort(reverse=True)

        def dfs(index):
            if index == len(matchsticks):
                return True

            for side_index in range(4):
                if sides[side_index] - matchsticks[index] >= 0:
                    sides[side_index] -= matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sides[side_index] += matchsticks[index]

                if (
                    sides[side_index] == side_length or
                    sides[side_index] == matchsticks[index]
                ):
                    break

            return False

        return dfs(0)


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: backtracking with pruning
        """
        total = sum(matchsticks)
        if total % 4:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        used = [False] * len(matchsticks)  # index is used

        def dfs(index, k, subset_sum):
            if subset_sum == target:
                return dfs(0, k - 1, 0)
            elif k == 0:
                return True

            for i in range(index, len(matchsticks)):
                if used[i] or subset_sum + matchsticks[i] > target:
                    continue
                used[i] = True
                if dfs(i + 1, k, subset_sum + matchsticks[i]):
                    return True
                used[i] = False

                if subset_sum == 0: # Pruning
                    return False

            return False

        return dfs(0, 4, 0)


print(Solution().makesquare([1, 1, 1, 1]) == True)
print(Solution().makesquare([1, 1, 2, 2, 2]) == True)
print(Solution().makesquare([3, 3, 3, 3, 4]) == False)
print(Solution().makesquare([3, 3, 2, 2, 2]) == False)
print(Solution().makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) == True)
print(Solution().makesquare([7215807, 6967211, 5551998, 6632092, 2802439, 821366, 2465584, 9415257, 8663937, 3976802, 2850841, 803069, 2294462, 8242205, 9922998]) == False)
print(Solution().makesquare([10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]) == True)