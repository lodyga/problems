class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """
        Time complexity: O(n * m)
            n: words length
            m: average word length
        Auxiliary space complexity: O(1)
        Tags: hash set
        """
        counter = len(words)
        allowed_set = set(allowed)
        for word in words:
            for letter in word:
                if letter not in allowed_set:
                    counter -= 1
                    break
        return counter


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """
        Time complexity: O(n * m)
            n: words length
            m: average word length
        Auxiliary space complexity: O(1)
        Tags: bit manipulation
        """
        def get_mask(word):
            bit_mask = 0
            for letter in word:
                letter_value = ord(letter) - ord("a")
                bit = 1 << letter_value
                bit_mask |= bit
            return bit_mask

        counter = len(words)
        bit_mask = get_mask(allowed)
        
        for word in words:
            for letter in word:
                letter_value = ord(letter) - ord("a")
                bit = 1 << letter_value
                if bit & bit_mask == 0:
                    counter -= 1
                    break

        return counter


print(Solution().countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]), 2)
print(Solution().countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]), 7)
print(Solution().countConsistentStrings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]), 4)