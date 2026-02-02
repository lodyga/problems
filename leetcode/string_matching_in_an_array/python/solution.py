class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """
        Time complexity: O(n4)
            O(n2 * t2)
            n: word count
            t: average word length
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: iteration
        """
        res = []

        for substring in words:
            for word in words:
                if (
                    len(substring) < len(word) and 
                    substring in word
                ):
                    res.append(substring)
                    break

        return res


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """
        Time complexity: O(n2 * t)
            n: words length
            t: average word length
        Auxiliary space complexity: O(n)
        Tags:
            DS: list
            A: Rabin-Karp, rolling hash, sliding window
        """        
        def is_substring(word: str, text: str) -> bool:
            if len(text) <= len(word):
                return False
            
            BASE = 29
            MOD = 10**9 + 7  # Large prime to avoid overflow.
            word_hash = 0
            
            for letter in word:
                letter_val = ord(letter) - ord("a")
                word_hash = (word_hash * BASE + letter_val) % MOD
            
            # POWER = BASE**(len(word) - 1)
            POWER = pow(BASE, len(word) - 1, MOD)
            sub_hash = 0
            left = 0
            
            for right, letter in enumerate(text):
                letter_val = ord(letter) - ord("a")
                sub_hash = (sub_hash * BASE + letter_val) % MOD

                if right < len(word) - 1:
                    continue

                if sub_hash == word_hash:
                    return True
                
                left_letter = text[left]
                left_letter_val = ord(left_letter) - ord("a")
                sub_hash = (sub_hash - left_letter_val * POWER) % MOD
                left += 1

            return False
        
        res = []
        for substr in words:
            for word in words:
                if is_substring(substr, word):
                    res.append(substr)
                    break

        return res


print(sorted(Solution().stringMatching(["bb", "cbb"])) == sorted(["bb"]))
print(sorted(Solution().stringMatching(["bb", "bbc"])) == sorted(["bb"]))
print(sorted(Solution().stringMatching(["hero", "shero"])) == sorted(["hero"]))
print(sorted(Solution().stringMatching(["mass", "as", "hero", "superhero"])) == sorted(["as", "hero"]))
print(sorted(Solution().stringMatching(["leetcode", "et", "code"])) == sorted(["et", "code"]))
print(sorted(Solution().stringMatching(["blue", "green", "bu"])) == sorted([]))
print(sorted(Solution().stringMatching(["axicc", "waxiccgq", "ssvob", "gissvobox", "zfzcj", "gtzfzcjyk", "cpjj","mnwaxiccgqd", "dvfoc", "rszfzcjim", "hxz", "vmssvob"])) == sorted(["axicc", "waxiccgq", "ssvob", "zfzcj"]))
