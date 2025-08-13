class Solution:
    def minWindow(self, text: str, word: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: sliding window
        """
        # stores the frequency of characters
        pattern = {}
        for letter in word:
            pattern[letter] = pattern.get(letter, 0) + 1
        
        left = 0
        # the number of unique letters left to match the pattern
        needed_match = len(pattern)
        # tracks character frequencies in the current sliding window
        window = {}
        # minium substring length
        substring_length = len(text) + 1
        # the start of the shortest window
        start = 0
        
        for right, letter in enumerate(text):

            if letter in pattern:
                window[letter] = window.get(letter, 0) + 1
                if window[letter] == pattern[letter]:
                    needed_match -= 1
            
            # while pattern is matched
            while needed_match == 0:
                # # if current string if shorter
                if right - left + 1 < substring_length:
                    substring_length = right - left + 1
                    start = left

                # Shrink the window:
                left_letter = text[left]
                if left_letter in pattern:
                    if window[left_letter] == pattern[left_letter]:
                        needed_match += 1
                    window[left_letter] -= 1
                left += 1

        return (text[start: start + substring_length] 
                if substring_length != len(text) + 1 
                else "")


print(Solution().minWindow("accbca", "ab") == "bca")
print(Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC")
print(Solution().minWindow("a", "a") == "a")
print(Solution().minWindow("a", "aa") == "")
print(Solution().minWindow("a", "b") == "")
print(Solution().minWindow("ab", "b") == "b")
print(Solution().minWindow("bba", "ab") == "ba")
print(Solution().minWindow("abc", "a") == "a")
print(Solution().minWindow("jwsdrkqzrthzysvqqazpfnulprulwmwhiqlbcdduxktxepnurpmxegktzegxscfbusexvhruumrydhvvyjucpeyrkeodjvgdnkalutfoizoliliguckmikdtpryanedcqgpkzxahwrvgcdoxiylqjolahjawpfbilqunnvwlmtrqxfphgaxroltyuvumavuomodblbnzvequmfbuganwliwidrudoqtcgyeuattxxlrlruhzuwxieuqhnmndciikhoehhaeglxuerbfnafvebnmozbtdjdo", "qruzywfhkcbovewle") == "vequmfbuganwliwidrudoqtcgyeuattxxlrlruhzuwxieuqhnmndciik")