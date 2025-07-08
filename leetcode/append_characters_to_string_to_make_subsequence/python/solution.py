class Solution:
    def appendCharacters(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(n)
            O(min(n+m))
        Auxiliary space complexity: O(n)
            O(min(n+m))
        Tags: dfs, recursion
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


class Solution:
    def appendCharacters(self, word1: str, word2: str) -> int:
        """
        Time complexity: O(n)
            O(min(n+m))
        Auxiliary space complexity: O(1)
        Tags: iteration, two pointers
        """
        index1 = 0
        index2 = 0

        while (
            index1 < len(word1) and 
            index2 < len(word2)
        ):
            if word1[index1] == word2[index2]:
                index2 += 1
            
            index1 += 1

        return len(word2) - index2

print(Solution().appendCharacters("coaching", "coding") == 4)
print(Solution().appendCharacters("abcde", "a") == 0)
print(Solution().appendCharacters("z", "abcde") == 5)
print(Solution().appendCharacters("a", "a") == 0)