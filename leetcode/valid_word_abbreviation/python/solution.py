class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers, string, iteration
        """
        index = 0
        index2 = 0
        while index < len(word) and index2 < len(abbr):
            if word[index] == abbr[index2]:
                index += 1
                index2 += 1
                continue
            elif abbr[index2].isdigit():
                if abbr[index2] == "0":
                    return False

                skip = 0
                while index2 < len(abbr) and abbr[index2].isdigit():
                    skip = skip*10 + int(abbr[index2])
                    index2 += 1
                index += skip
            else:
                return False
        
        return index == len(word) and index2 == len(abbr)


print(Solution().validWordAbbreviation("internationalization", "i12iz4n"), True)
print(Solution().validWordAbbreviation("apple", "a2e"), False)
print(Solution().validWordAbbreviation("substitution", "s010n"), False)