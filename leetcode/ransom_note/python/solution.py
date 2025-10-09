class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        letters = [0] * 26
        for letter in magazine:
            letters[ord(letter) - ord("a")] += 1
        for letter in ransomNote:
            index = ord(letter) - ord("a")
            if letters[index] == 0:
                return False
            letters[index] -= 1
        return True


print(Solution().canConstruct("a", "b") == False)
print(Solution().canConstruct("aa", "ab") == False)
print(Solution().canConstruct("aa", "aab") == True)