class Solution:
    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: iteration
        """
        if not len(sentence1) == len(sentence2):
            return False

        similar_word = {(word1, word2) for (word1, word2) in similarPairs}

        for index in range(len(sentence1)):
            word1 = sentence1[index]
            word2 = sentence2[index]

            if (
                word1 != word2 and
                (
                    (word1, word2) not in similar_word and
                    (word2, word1) not in similar_word
                )
            ):
                return False

        return True


print(Solution().areSentencesSimilar(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "fine"], ["drama", "acting"], ["skills", "talent"]]) == True)
print(Solution().areSentencesSimilar(["great"], ["great"], []) == True)
print(Solution().areSentencesSimilar(["great"], ["doubleplus", "good"], [["great", "doubleplus"]]) == False)
