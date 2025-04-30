class Solution:
    def isSubsequence(self, word_1: str, word_2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        if not word_1:
            return True

        index = 0
        for letter in word_2:
            if letter == word_1[index]:
                index += 1
            if index == len(word_1):
                return True

        return False


print(Solution().isSubsequence("", ""), True)
print(Solution().isSubsequence("", "ahbgdc"), True)
print(Solution().isSubsequence("abc", "ahbgdc"), True)
print(Solution().isSubsequence("axc", "ahbgdc"), False)
