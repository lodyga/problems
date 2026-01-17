class Solution:
    def gcdOfStrings(self, text1: str, text2: str) -> str:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags:
            DS: string
            A: iteration
        """
        def is_gcd(text, sub_text):
            text_len = len(text)
            subtext_len = len(sub_text)

            if text_len % subtext_len:
                return False

            for index in range(text_len):
                if text[index] != sub_text[index % subtext_len]:
                    return False
            return True

        N1 = len(text1)
        N2 = len(text2)
        for next_len in range(min(N1, N2), 0, -1):
            if N1 % next_len or N2 % next_len:
                continue
            elif (
                is_gcd(text2, text2[: next_len]) and
                is_gcd(text1, text2[: next_len])
            ):
                return text2[: next_len]

        return ""


print(Solution().gcdOfStrings("AA", "A") == "A")
print(Solution().gcdOfStrings("ABCABC", "ABC") == "ABC")
print(Solution().gcdOfStrings("ABABAB", "ABAB") == "AB")
print(Solution().gcdOfStrings("ABABABAB", "ABAB") == "ABAB")
print(Solution().gcdOfStrings("LEFT", "CODY") == "")
print(Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX")
