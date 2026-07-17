class Solution:
    def appendCharacters(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, iteration
        """
        idx2 = 0
        text2_len = len(text2)

        for letter in text1:
            if idx2 == text2_len:
                return 0
            elif letter == text2[idx2]:
                idx2 += 1

        return text2_len - idx2


print(Solution().appendCharacters("coaching", "coding") == 4)
print(Solution().appendCharacters("abcde", "a") == 0)
print(Solution().appendCharacters("z", "abcde") == 5)
print(Solution().appendCharacters("a", "a") == 0)
