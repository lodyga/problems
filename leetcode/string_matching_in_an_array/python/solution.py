class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """
        Time complexity: O(n2 * t2)
            n: words length
            t: average word length
        Auxiliary space complexity: O(n)
        Tags: hash set
        """
        word_set = set(words)
        substring_words = []

        for pattern in word_set:
            for word in word_set:
                if (
                    pattern == word or
                    len(pattern) >= len(word)
                ):
                    continue
                elif pattern in word:
                    substring_words.append(pattern)
                    break

        return substring_words


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """
        Time complexity: O(n2 * t)
            n: words length
            t: average word length
        Auxiliary space complexity: O(n)
        Tags: Rabin-Karp, sliding window
        """
        word_set = set(words)
        substring_words = []
        base = 29

        def rabin_krap(pattern, text) -> bool:
            pattern_length = len(pattern)
            pattern_hash = 0
            text_hash = 0
            power = 1
            mod = 10**9 + 7  # Large prime to avoid overflow

            # Calculate pattern hash and initial text window hash
            for index in range(pattern_length):
                pattern_hash = (pattern_hash * base + (ord(pattern[index]) - ord("a"))) % mod
                text_hash = (text_hash * base + (ord(text[index]) - ord("a"))) % mod
                if index:
                    power = (power * base) % mod

            # Sliding window
            for left in range(len(text) - pattern_length + 1):
                right = left + pattern_length

                if pattern_hash == text_hash:
                    return True
                elif left < len(text) - pattern_length:
                    # subtract left number
                    text_hash = (text_hash - (ord(text[left]) - ord("a")) * power) % mod
                    # handle negative hash
                    # if text_hash < 0:
                    #     text_hash += mod
                    # shif left and add right number
                    text_hash = (text_hash * base + ord(text[right]) - ord("a")) % mod

            return False

        for pattern in word_set:
            for word in word_set:
                if (
                    pattern == word or
                    len(pattern) >= len(word)
                ):
                    continue
                if rabin_krap(pattern, word):
                    substring_words.append(pattern)
                    break

        return substring_words


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """
        Time complexity: O(n2 * t)
            n: words length
            t: average word length
        Auxiliary space complexity: O(n)
        Tags: Rabin-Karp, sliding window
        """
        # word_set = set(words)
        words.sort(key=len)
        substring_words = []
        base = 29

        def rabin_krap(pattern, text) -> bool:
            pattern_length = len(pattern)
            pattern_hash = 0
            text_hash = 0
            power = 1
            mod = 10**9 + 7  # Large prime to avoid overflow

            # Calculate pattern hash and initial text window hash
            for index in range(pattern_length):
                pattern_hash = (pattern_hash * base + (ord(pattern[index]) - ord("a"))) % mod
                text_hash = (text_hash * base + (ord(text[index]) - ord("a"))) % mod
                if index:
                    power = (power * base) % mod

            # Sliding window
            for left in range(len(text) - pattern_length + 1):
                right = left + pattern_length

                if pattern_hash == text_hash:
                    return True
                elif left < len(text) - pattern_length:
                    # subtract left number
                    text_hash = (text_hash - (ord(text[left]) - ord("a")) * power) % mod
                    # handle negative hash
                    # if text_hash < 0:
                    #     text_hash += mod
                    # shif left and add right number
                    text_hash = (text_hash * base + ord(text[right]) - ord("a")) % mod

            return False

        for index, pattern in enumerate(words):
            for word_index in range(index + 1, len(words)):
                word = words[word_index]
                if len(pattern) == len(word):
                    continue
                elif rabin_krap(pattern, word):
                    substring_words.append(pattern)
                    break

        return substring_words


print(Solution().stringMatching(["bb", "cbb"]), ["bb"])
print(Solution().stringMatching(["bb", "bbc"]), ["bb"])
print(Solution().stringMatching(["hero", "shero"]), ["hero"])
print(Solution().stringMatching(["mass", "as", "hero", "superhero"]), ["as", "hero"])
print(Solution().stringMatching(["leetcode", "et", "code"]), ["et", "code"])
print(Solution().stringMatching(["blue", "green", "bu"]), [])
print(Solution().stringMatching(["axicc", "waxiccgq", "ssvob", "gissvobox", "zfzcj", "gtzfzcjyk", "cpjj", "mnwaxiccgqd", "dvfoc", "rszfzcjim", "hxz", "vmssvob"]), ["axicc", "waxiccgq", "ssvob", "zfzcj"])