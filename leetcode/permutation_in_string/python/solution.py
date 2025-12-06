class Solution:
    def checkInclusion(self, word: str, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: hash map
            A: sliding window 
        """
        pattern = {}
        for letter in word:
            pattern[letter] = pattern.get(letter, 0) - 1

        left = 0
        for right, letter in enumerate(text):
            pattern[letter] = pattern.get(letter, 0) + 1
            if pattern[letter] == 0:
                pattern.pop(letter)

            if right + 1 < len(word):
                continue

            if len(pattern) == 0:
                return True

            left_letter = text[left]
            pattern[left_letter] = pattern.get(left_letter, 0) - 1
            if pattern[left_letter] == 0:
                pattern.pop(left_letter)
            left += 1

        return False


class Solution2:
    def checkInclusion(self, word1: str, word2: str) -> bool:
        left = 0
        pattern = {}

        for letter in word1:
            pattern[letter] = pattern.get(letter, 0) + 1

        # `need` keeps track of how many characters in `pattern` are still needed to match frequencies in `window`
        need = len(pattern)
        # sliding window
        letter_frequency = {}

        for right, letter in enumerate(word2):
            if letter in pattern:
                letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

                if letter_frequency[letter] == pattern[letter]:
                    need -= 1

                if right - left + 1 == len(word1):
                    if need == 0:
                        return True

                    left_letter = word2[left]
                    if letter_frequency[left_letter] == pattern[left_letter]:
                        need += 1
                    letter_frequency[left_letter] -= 1
                    left += 1

            else:
                need = len(pattern)
                letter_frequency.clear()
                left = right + 1

        return False


class Solution3:
    def checkInclusion(self, word1: str, word2: str) -> bool:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(n)
        Tags: brute-froce
        """
        pattern = {}
        for letter in word1:
            pattern[letter] = pattern.get(letter, 0) + 1

        for left in range(len(word2) - len(word1) + 1):
            pattern_copy = pattern.copy()

            for right in range(left, left + len(word1)):
                letter = word2[right]
                if letter not in pattern_copy:
                    break
                pattern_copy[letter] -= 1
                if pattern_copy[letter] == 0:
                    pattern_copy.pop(letter)

            if not pattern_copy:
                return True

        return False


print(Solution().checkInclusion("ab", "cba") == True)
print(Solution().checkInclusion("ab", "eidbaooo") == True)
print(Solution().checkInclusion("ab", "eidboaoo") == False)
print(Solution().checkInclusion("ccc", "cbac") == False)
print(Solution().checkInclusion("ab", "a") == False)
print(Solution().checkInclusion("abcdxabcde", "abcdeabcdx") == True)
print(Solution().checkInclusion("adc", "dcda") == True)
print(Solution().checkInclusion("hello", "ooolleoooleh") == False)
print(Solution().checkInclusion("mart", "karma") == False)
print(Solution().checkInclusion("abc", "ccccbbbbaaaa") == False)
