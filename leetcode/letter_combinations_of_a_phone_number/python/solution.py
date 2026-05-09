class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Time complexity: O(n4^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        """
        N = len(digits)
        combination = []
        res = []
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(idx: int) -> None:
            if idx == N:
                res.append("".join(combination))
                return

            for letter in digit_to_letter[digits[idx]]:
                combination.append(letter)
                backtrack(idx + 1)
                combination.pop()

        backtrack(0)
        return res


print(Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
print(Solution().letterCombinations("2") == ["a", "b", "c"])
