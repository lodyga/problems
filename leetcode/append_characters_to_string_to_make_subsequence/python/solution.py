class Solution:
    def appendCharacters(self, text1: str, text2: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, iteration
        """
        index1 = 0
        index2 = 0

        while index1 < len(text1) and index2 < len(text2):
            if text1[index1] == text2[index2]:
                index2 += 1

            index1 += 1

        return len(text2) - index2


class Solution:
    def appendCharacters(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: two pointers, recursion
        """
        def dfs(index1, index2):
            if (
                index1 == len(word1) or
                index2 == len(word2)
            ):
                return 0
            elif word1[index1] == word2[index2]:
                return dfs(index1 + 1, index2 + 1) + 1
            else:
                return dfs(index1 + 1, index2)

        return len(word2) - dfs(0, 0)


print(Solution().appendCharacters("coaching", "coding") == 4)
print(Solution().appendCharacters("abcde", "a") == 0)
print(Solution().appendCharacters("z", "abcde") == 5)
print(Solution().appendCharacters("a", "a") == 0)
