class Solution:
    def isIsomorphic(self, word_1: str, word_2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: hash map
        """
        if len(word_1) != len(word_2):
            return False
        
        letter_1_map_letter_2 = {}
        letters_2 = set()

        for index in range(len(word_1)):
            letter_1 = word_1[index]
            letter_2 = word_2[index]

            if word_1[index] in letter_1_map_letter_2:
                if letter_1_map_letter_2[letter_1] != letter_2:
                    return False
            else:
                if letter_2 in letters_2:
                    return False
                letter_1_map_letter_2[letter_1] = letter_2
                letters_2.add(letter_2)

        return True


print(Solution().isIsomorphic("egg", "add"), True)
print(Solution().isIsomorphic("foo", "bar"), False)
print(Solution().isIsomorphic("paper", "title"), True)
print(Solution().isIsomorphic("badc", "baba"), False)