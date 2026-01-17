class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        Time complexity: O(n4^n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: DFS with backtracking
        """
        combination = []
        combination_list = []
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

        def backtrack(index):
            if index == len(digits):
                combination_list.append("".join(combination))
                return

            digit = digits[index]
            for letter in digit_to_letter[digit]:
                combination.append(letter)
                backtrack(index + 1)
                combination.pop()

        backtrack(0)
        return combination_list


print(Solution().letterCombinations("2") == ["a", "b", "c"])
print(Solution().letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
