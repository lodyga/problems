class Solution:
    def combinationSum3(self, combination_length: int, total: int) -> list[list[int]]:
        """
        Time complexity: O(1)
            O(2^9)
        Auxiliary space complexity: O(1)
        Tags: backtracking
        """
        combination = []
        combination_list = []

        def dfs(digit):
            if (len(combination) == combination_length and
                    sum(combination) == total):
                combination_list.append(combination.copy())
                return
            elif (digit == 10 or
                  len(combination) > combination_length or
                  sum(combination) > total):
                return

            combination.append(digit)
            dfs(digit + 1)
            combination.pop()
            dfs(digit + 1)

        dfs(1)
        return combination_list


print(Solution().combinationSum3(3, 7) == [[1, 2, 4]])
print(Solution().combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
print(Solution().combinationSum3(4, 1) == [])