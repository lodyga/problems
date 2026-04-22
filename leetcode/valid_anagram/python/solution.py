class Solution:
    def isAnagram(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        if len(text1) != len(text2):
            return False

        letter_freq = [0] * 26

        for letter in text1:
            idx = ord(letter) - ord("a")
            letter_freq[idx] += 1

        for letter in text2:
            idx = ord(letter) - ord("a")
            letter_freq[idx] -= 1

            if letter_freq[idx] == -1:
                return False

        return True


class Solution:
    def isAnagram(self, text1: str, text2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: hash map
            A: iteration
        """
        if len(text1) != len(text2):
            return False

        letter_freq = {}

        for letter in text1:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1

        for letter in text2:
            if letter_freq.get(letter, 0) == 0:
                return False

            letter_freq[letter] = letter_freq[letter] - 1

        return True


class Solution:
        def isAnagram(self, text_1: str, text_2: str) -> bool:
            """
            Time complexity: O(n)
            Auxiliary space complexity: O(1)
            Tags:
                DS: hash map
                A: build-in function
            """
            from collections import Counter
            
            if len(text_1) != len(text_2):
                return False

            return Counter(text_1) == Counter(text_2)


print(Solution().isAnagram("anagram", "nagaram") == True)
print(Solution().isAnagram("rat", "car") == False)
print(Solution().isAnagram("", "") == True)
