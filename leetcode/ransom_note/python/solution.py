class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        letters = [0] * 26

        for letter in magazine:
            letter_ind = ord(letter) - ord("a")
            letters[letter_ind] += 1

        for letter in ransom_note:
            letter_ind = ord(letter) - ord("a")

            if letters[letter_ind] == 0:
                return False

            letters[letter_ind] -= 1

        return True


print(Solution().canConstruct("a", "b") == False)
print(Solution().canConstruct("aa", "ab") == False)
print(Solution().canConstruct("aa", "aab") == True)
