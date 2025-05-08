class Solution:
    def isAlienSorted(self, word_list: list[str], order) -> bool:
        """
        Time complexity: O(n*k)
            n: word number
            k: avg word length
        Auxiliary space complexity: O(1)
        """
        def are_words_in_order(word1, word2):
            for index in range(min(len(word1), len(word2))):
                if letter_order[word1[index]] < letter_order[word2[index]]:
                    return True
                elif letter_order[word1[index]] > letter_order[word2[index]]:
                    return False
            return len(word1) <= len(word2)

        letter_order = {letter: index 
                        for index, letter 
                        in enumerate(order)}

        for index in range(len(word_list) - 1):
            if not are_words_in_order(word_list[index], word_list[index + 1]):
                return False
        
        return True


print(Solution().isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), True)
print(Solution().isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"), False)
print(Solution().isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz"), False)
print(Solution().isAlienSorted(["ubg", "kwh"], "qcipyamwvdjtesbghlorufnkzx"), True)