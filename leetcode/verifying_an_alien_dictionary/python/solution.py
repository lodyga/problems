class Solution:
    def isAlienSorted(self, words: list[str], order) -> bool:
        """
        Time complexity: O(n*k)
            n: word count
            k: avg word length
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map, string
            A: iteration
        """
        letter_index = {letter: index for index, letter in enumerate(order)}

        for index in range(len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]

            for i2 in range(len(word1)):
                if (
                    i2 == len(word2) or
                    letter_index[word1[i2]] > letter_index[word2[i2]]
                ):
                    return False
                elif letter_index[word1[i2]] < letter_index[word2[i2]]:
                    break
        
        return True


print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True)
print(Solution().isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") == False)
print(Solution().isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") == False)
print(Solution().isAlienSorted(["ubg", "kwh"], "qcipyamwvdjtesbghlorufnkzx") == True)
print(Solution().isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz") == True)
