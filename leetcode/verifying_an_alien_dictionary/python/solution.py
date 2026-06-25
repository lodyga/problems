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
        def are_two_words_sorted(word1: str, word2: str) -> bool:
            for idx in range(max(len(word1), len(word2))):
                if idx == len(word1):
                    return True
                elif idx == len(word2):
                    return False

                letter1 = word1[idx]
                letter2 = word2[idx]

                if letter1 == letter2:
                    continue
                elif letter_idx[letter1] < letter_idx[letter2]:
                    return True
                else:  # elif letter_idx[letter1] > letter_idx[letter2]:
                    return False

            return True

        N = len(words)
        letter_idx = {letter: idx
                      for idx, letter in enumerate(order)}

        for idx in range(N - 1):
            word1 = words[idx]
            word2 = words[idx + 1]

            if not are_two_words_sorted(word1, word2):
                return False

        return True


print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True)
print(Solution().isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") == False)
print(Solution().isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") == False)
print(Solution().isAlienSorted(["ubg", "kwh"], "qcipyamwvdjtesbghlorufnkzx") == True)
print(Solution().isAlienSorted(["kuvp", "q"], "ngxlkthsjuoqcpavbfdermiywz") == True)
print(Solution().isAlienSorted(["hello","hello"], "abcdefghijklmnopqrstuvwxyz") == True)
