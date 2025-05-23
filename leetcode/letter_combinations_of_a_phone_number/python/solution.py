class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Time complexity: O(n4^n)
            Up to 4 letters in one digit
        Auxiliary space complexity: O(n)
        Tags: iteration dfs with backtracking
        """
        if not digits:
            return []
        combination = []
        combinationList = []
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

        def dfs(index):
            if index == len(digits):
                combinationList.append("".join(combination))
                return

            digit = digits[index]
            for letter in digit_to_letter[digit]:
                combination.append(letter)
                dfs(index + 1)
                combination.pop()

        dfs(0)
        return combinationList


print(Solution().letterCombinations("2") == ["a", "b", "c"])
print(Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
print(Solution().letterCombinations("") == [])