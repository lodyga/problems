class Solution:
    def wordPattern(self, pattern: str, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash map, hash set
        """
        word_list = text.split()
        unique_words = set()
        letter_to_word_map = {}
        if len(pattern) != len(word_list):
            return False

        for index, letter in enumerate(pattern):
            if letter not in letter_to_word_map:
                if word_list[index] in unique_words:
                    return False
                letter_to_word_map[letter] = word_list[index]
                unique_words.add(word_list[index])
            else:
                if letter_to_word_map[letter] != word_list[index]:
                    return False
        
        return True


print(Solution().wordPattern("abba", "dog cat cat dog"), True)
print(Solution().wordPattern("abba", "dog cat cat fish"), False)
print(Solution().wordPattern("aaaa", "dog cat cat dog"), False)
print(Solution().wordPattern("abba", "dog dog dog dog"), False)