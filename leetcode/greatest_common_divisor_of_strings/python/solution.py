class Solution:
    def gcdOfStrings(self, text1: str, text2: str) -> str:
        def is_gcd(text: str, sub_text: str) -> bool:
            text_len = len(text)
            sub_text_len = len(sub_text)

            if text_len % sub_text_len:
                return False

            repeat_counter = text_len // sub_text_len

            return text == sub_text * repeat_counter

        N1 = len(text1)
        N2 = len(text2)

        for curr_len in range(min(N1, N2), 0, -1):
            if (N1 % curr_len or N2 % curr_len):
                continue
            elif (
                is_gcd(text1, text1[: curr_len])
                and is_gcd(text2, text1[: curr_len])
            ):
                return text1[: curr_len]

        return ""


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

            for idx in range(text_len):
                if text[idx] != sub_text[idx % subtext_len]:
                    return False
            
            return True

        N1 = len(text1)
        N2 = len(text2)

        for curr_len in range(min(N1, N2), 0, -1):
            if (N1 % curr_len or N2 % curr_len):
                continue
            elif (
                is_gcd(text2, text2[: curr_len])
                and is_gcd(text1, text2[: curr_len])
            ):
                return text2[: curr_len]

        return ""


print(Solution().gcdOfStrings("ABCABC", "ABC") == "ABC")
print(Solution().gcdOfStrings("ABABAB", "ABAB") == "AB")
print(Solution().gcdOfStrings("LEFT", "CODY") == "")
print(Solution().gcdOfStrings("AA", "A") == "A")
print(Solution().gcdOfStrings("ABABABAB", "ABAB") == "ABAB")
print(Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX")
