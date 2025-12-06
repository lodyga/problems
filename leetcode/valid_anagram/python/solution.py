from collections import Counter


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
        
        letter_frequency = [0] * 26
        for letter in text1:
            index = ord(letter) - ord("a")
            letter_frequency[index] += 1
        for letter in text2:
            index = ord(letter) - ord("a")
            if letter_frequency[index] == 0:
                return False
            else:
                letter_frequency[index] -= 1
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
        
        letter_frequency = {}
        for letter in text1:
            letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
        for letter in text2:
            if letter in letter_frequency:
                letter_frequency[letter] -= 1
                if letter_frequency[letter] == 0:
                    letter_frequency.pop(letter)
            else:
                return False
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
            if len(text_1) != len(text_2):
                return False
            return Counter(text_1) == Counter(text_2)


print(Solution().isAnagram("anagram", "nagaram") == True)
print(Solution().isAnagram("rat", "car") == False)
print(Solution().isAnagram("", "") == True)
