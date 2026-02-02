class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """
        Time complexity: O(n·m)
            O(n·m·26)
            n: words length
            m: average word length
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        counter = len(words)
        
        for word in words:
            for letter in word:
                if letter not in allowed:
                    counter -= 1
                    break

        return counter


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """
        Time complexity: O(n·m)
            n: words length
            m: average word length
        Auxiliary space complexity: O(1)
        Tags:
            A: iteration
        """
        counter = len(words)
        all_set = set(allowed)
        
        for word in words:
            for letter in word:
                if letter not in all_set:
                    counter -= 1
                    break

        return counter


class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        """
        Time complexity: O(n·m)
            n: words length
            m: average word length
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        def get_mask(word):
            mask = 0
            for letter in word:
                index = ord(letter) - ord("a")
                bit = 1 << index
                mask |= bit
            return mask
        
        bit_mask = get_mask(allowed)
        counter = len(words)

        for word in words:
            for letter in word:
                index = ord(letter) - ord("a")
                bit = 1 << index

                if bit & bit_mask == 0:
                    counter -= 1
                    break
        
        return counter


print(Solution().countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2)
print(Solution().countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7)
print(Solution().countConsistentStrings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == 4)
