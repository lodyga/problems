from collections import Counter


class Solution:
    def is_anagram_using_count_array(self, text_1: str, text_2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Algorithm: Hash Table Frequency Counter
        """
        if len(text_1) != len(text_2):
            return False
        frequencies = [0] * 26

        for index in range(len(text_1)):
            frequencies[ord(text_1[index]) - ord("a")] += 1
            frequencies[ord(text_2[index]) - ord("a")] -= 1
        for frequency in frequencies:
            if frequency:
                return False
        return True

    def is_anagram_using_dict(self, text_1: str, text_2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1) | (lowercase English letters)
        Algorithm: Dictionary Frequency Counter
        """
        if len(text_1) != len(text_2):
            return False
        text_1_letter_counter = self.counter(text_1)
        text_2_letter_counter = self.counter(text_2)
        return text_1_letter_counter == text_2_letter_counter

    def counter(self, text: str) -> dict:
        letter_counter = {}
        for letter in text:
            letter_counter[letter] = letter_counter.get(letter, 0) + 1
        return letter_counter

    def is_anagram_using_collections_counter(self, text_1: str, text_2: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1) | (lowercase English letters)
        Algorithm: Dictionary Frequency Counter with collections counter
        """
        if len(text_1) != len(text_2):
            return False
        return Counter(text_1) == Counter(text_2)

    def is_anagram_using_sorting(self, text_1: str, text_2: str) -> bool:
        """
        Time complexity: O(nlogn)
        Auxiliary space complexity: O(n)
        Algorithm: Sorting Comparison
        """
        if len(text_1) != len(text_2):
            return False
        text_1_letter_counter = sorted(text_1)
        text_2_letter_counter = sorted(text_2)
        return text_1_letter_counter == text_2_letter_counter


print(Solution().is_anagram_using_count_array("anagram", "nagaram") == True)
print(Solution().is_anagram_using_count_array("rat", "car") == False)
print(Solution().is_anagram_using_count_array("", "") == True)
