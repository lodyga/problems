class Solution:
    def wordPattern(self, pattern: str, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map, hash set
            A: iteration
        """
        words = text.split(" ")
        letter_to_word = {}
        word_set = set()

        if len(pattern) != len(words):
            return False

        for letter, word in zip(pattern, words):
            if letter in letter_to_word:
                if letter_to_word[letter] != word:
                    return False

            elif word in word_set:
                return False

            else:
                letter_to_word[letter] = word
                word_set.add(word)

        return True


print(Solution().wordPattern("abba", "dog cat cat dog") == True)
print(Solution().wordPattern("abba", "dog cat cat fish") == False)
print(Solution().wordPattern("aaaa", "dog cat cat dog") == False)
print(Solution().wordPattern("abba", "dog dog dog dog") == False)
print(Solution().wordPattern("aaa", "aa aa aa aa") == False)
