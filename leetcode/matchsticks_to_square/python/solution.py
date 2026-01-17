class Solution:
    def makesquare(self, sticks: list[int]) -> bool:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: array
            A: backtracking with pruning, sorting
        """
        perimeter = sum(sticks)
        if perimeter % 4:
            return False
        side = perimeter // 4
        sticks.sort(reverse=True)
        sides = [0, 0, 0, 0]

        def backtrack(start):
            if start == len(sticks):
                return True

            stick = sticks[start]

            for index in range(4):
                if sides[index] + stick <= side:
                    sides[index] += stick
                    if backtrack(start + 1):
                        return True
                    sides[index] -= stick

                # pruning
                if sides[index] == 0:
                    break
            return False

        return backtrack(0)


print(Solution().makesquare([1, 1, 1, 1]) == True)
print(Solution().makesquare([1, 1, 2, 2, 2]) == True)
print(Solution().makesquare([3, 3, 3, 3, 4]) == False)
print(Solution().makesquare([3, 3, 2, 2, 2]) == False)
print(Solution().makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]) == True)
print(Solution().makesquare([10, 6, 5, 5, 5, 3, 3, 3, 2, 2, 2, 2]) == True)
print(Solution().makesquare([7215807, 6967211, 5551998, 6632092, 2802439, 821366, 2465584, 9415257, 8663937, 3976802, 2850841, 803069, 2294462, 8242205, 9922998]) == False)
