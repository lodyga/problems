class Solution:
    def minWindow(self, text: str, word: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: sliding window
        """
        window = {}
        left = 0
        res_len = len(text) + 1
        start = len(text)

        for letter in word:
            window[letter] = window.get(letter, 0) - 1

        needed = len(window)

        for right, letter in enumerate(text):
            if letter not in window:
                continue

            window[letter] = window.get(letter, 0) + 1

            if window.get(letter) == 0:
                needed -= 1

            while needed == 0:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    start = left

                left_letter = text[left]

                if left_letter in window:
                    if window[left_letter] == 0:
                        needed += 1

                    window[left_letter] -= 1

                left += 1

        if start == len(text):
            return ""
        else:
            return text[start: start + res_len]


print(Solution().minWindow("a", "a") == "a")
print(Solution().minWindow("a", "aa") == "")
print(Solution().minWindow("ab", "ab") == "ab")
print(Solution().minWindow("a", "b") == "")
print(Solution().minWindow("ab", "b") == "b")
print(Solution().minWindow("bba", "ab") == "ba")
print(Solution().minWindow("abc", "a") == "a")
print(Solution().minWindow("accbca", "ab") == "bca")
print(Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC")
print(Solution().minWindow("jwsdrkqzrthzysvqqazpfnulprulwmwhiqlbcdduxktxepnurpmxegktzegxscfbusexvhruumrydhvvyjucpeyrkeodjvgdnkalutfoizoliliguckmikdtpryanedcqgpkzxahwrvgcdoxiylqjolahjawpfbilqunnvwlmtrqxfphgaxroltyuvumavuomodblbnzvequmfbuganwliwidrudoqtcgyeuattxxlrlruhzuwxieuqhnmndciikhoehhaeglxuerbfnafvebnmozbtdjdo", "qruzywfhkcbovewle") == "vequmfbuganwliwidrudoqtcgyeuattxxlrlruhzuwxieuqhnmndciik")
