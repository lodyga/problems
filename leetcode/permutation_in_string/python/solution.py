class Solution:
    def checkInclusion(self, word: str, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: sliding window 
        """
        window = [0] * 26
        left = 0

        for letter in word:
            idx = ord(letter) - ord("a")
            window[idx] -= 1

        for right, letter in enumerate(text):
            idx = ord(letter) - ord("a")
            window[idx] += 1

            if right - left + 1 < len(word):
                continue

            elif not any(window):
                return True

            left_letter = text[left]
            idx = ord(left_letter) - ord("a")
            window[idx] -= 1
            left += 1

        return False


class Solution:
    def checkInclusion(self, word: str, text: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: sliding window 
        """
        window = {}
        left = 0

        for letter in word:
            window[letter] = window.get(letter, 0) - 1

        for right, letter in enumerate(text):
            window[letter] = window.get(letter, 0) + 1

            if window[letter] == 0:
                window.pop(letter)

            if right - left + 1 < len(word):
                continue

            elif not window:
                return True

            left_letter = text[left]
            window[left_letter] = window.get(left_letter, 0) - 1
            if window[left_letter] == 0:
                window.pop(left_letter)
            left += 1

        return False


class Solution:
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
