class Solution:
    def minWindow(self, text: str, word: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: hash map
            A: sliding window
        """
        pattern = {}
        for letter in word:
            pattern[letter] = pattern.get(letter, 0) + 1

        left = 0
        window = {}
        start = -1
        shortest = len(text)
        needed = len(pattern)
        
        for right, letter in enumerate(text):
            window[letter] = window.get(letter, 0) + 1
            if (
                letter in pattern and
                window[letter] == pattern[letter]
            ):
                needed -= 1

            if needed:
                continue

            while needed == 0:
                window_length = right - left + 1
                if window_length <= shortest:
                    shortest = window_length
                    start = left

                left_letter = text[left]
                if (
                    left_letter in pattern and
                    window[left_letter] == pattern[left_letter]
                ):
                    needed += 1
                window[left_letter] -= 1
                left += 1

        return text[start: start + shortest]


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
