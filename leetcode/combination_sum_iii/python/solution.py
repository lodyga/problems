class Solution:
    def combinationSum3(self, k: int, target: int) -> list[list[int]]:
        """
        Time complexity: O(1)
            O(2^9)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: list
            A: DFS with backtracking
        """
        combination = []
        combination_list = []

        def bracktrack(index, total):
            if (
                total == target and
                len(combination) == k
            ):
                return combination_list.append(combination.copy())
            elif (
                index == 10 or
                total >= target or
                len(combination) == k
            ):
                return

            combination.append(index)
            bracktrack(index + 1, total + index)
            combination.pop()
            bracktrack(index + 1, total)

        bracktrack(1, 0)
        return combination_list

    def combinationSum3(self, k: int, target: int) -> list[list[int]]:
        """
        Time complexity: O(1)
            O(2^9)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: list
            A: DFS with backtracking
        """
        combination = []
        combination_list = []

        def bracktrack(index, total):
            if (
                total == target and
                len(combination) == k
            ):
                return combination_list.append(combination.copy())
            elif (
                index == 10 or
                total >= target or
                len(combination) == k
            ):
                return

            for i2 in range(index, 10):
                combination.append(i2)
                bracktrack(i2 + 1, total + i2)
                combination.pop()

        bracktrack(1, 0)
        return combination_list


print(Solution().combinationSum3(2, 4) == [[1, 3]])
print(Solution().combinationSum3(3, 7) == [[1, 2, 4]])
print(Solution().combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]])
print(Solution().combinationSum3(4, 1) == [])
