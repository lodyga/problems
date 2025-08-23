class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: string
        """
        def is_gdc(text, cd):
            index = 0
            while index < len(text):
                if cd != text[index: index + len(cd)]:
                    return False
                index += len(cd)
            return True

        for index in reversed(range(min(len(str2), len(str1)))):
            if len(str1) % (index + 1) or len(str1) % (index + 1):
                continue
            
            cd = str2[:index + 1]
            
            if is_gdc(str1, cd) and is_gdc(str2, cd):
                return cd

        return ""


print(Solution().gcdOfStrings("AA", "A") == "A")
print(Solution().gcdOfStrings("ABCABC", "ABC") == "ABC")
print(Solution().gcdOfStrings("ABABAB", "ABAB") == "AB")
print(Solution().gcdOfStrings("LEFT", "CODY") == "")
print(Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX")