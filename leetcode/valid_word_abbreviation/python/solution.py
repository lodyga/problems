class Solution:
    def validWordAbbreviation(self, text: str, abbr: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, iteration
        """
        i1 = i2 = 0

        while i1 < len(text) and i2 < len(abbr):
            if text[i1] == abbr[i2]:
                i1 += 1
                i2 += 1

            elif "0" <= abbr[i2] <= "9":
                if abbr[i2] == "0":
                    return False

                skip = 0
                while i2 < len(abbr) and "0" <= abbr[i2] <= "9":
                    skip = skip*10 + int(abbr[i2])
                    i2 += 1
                i1 += skip

            else:
                return False

        return i1 == len(text) and i2 == len(abbr)


print(Solution().validWordAbbreviation("apple", "a2le") == True)
print(Solution().validWordAbbreviation("appl", "a2le") == False)
print(Solution().validWordAbbreviation("apple", "a2e") == False)
print(Solution().validWordAbbreviation("internationalization", "i12iz4n") == True)
print(Solution().validWordAbbreviation("substitution", "s010n") == False)
