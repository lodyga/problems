class Solution:
    def isIsomorphic(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: hash map
            A: iteration
        """
        if len(text1) != len(text2):
            return False

        def is_iso(text1, text2):
            letter_map = {}
            for letter1, letter2 in zip(text1, text2):
                if letter1 in letter_map:
                    if letter_map[letter1] != letter2:
                        return False
                else:
                    letter_map[letter1] = letter2
            return True

        return is_iso(text1, text2) and is_iso(text2, text1)


print(Solution().isIsomorphic("egg", "add") == True)
print(Solution().isIsomorphic("foo", "bar") == False)
print(Solution().isIsomorphic("paper", "title") == True)
print(Solution().isIsomorphic("badc", "baba") == False)
