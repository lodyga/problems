class Solution:
    def countGoodSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: hash map
        """
        char_frequency = {}
        good_string_counter = 0

        for index, char in enumerate(text):
            char_frequency[char] = char_frequency.get(char, 0) + 1

            if index > 1:
                if len(char_frequency) == 3:
                    good_string_counter += 1

                char_frequency[text[index - 2]] -= 1
                if not char_frequency[text[index - 2]]:
                    char_frequency.pop(text[index - 2])

        return good_string_counter

    def countGoodSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: hash set
        """
        good_string_counter = 0

        for index in range(len(text) - 2):
            if len(set(text[index: index + 3])) == 3:
                good_string_counter += 1
        
        return good_string_counter


print(Solution().countGoodSubstrings("xyzzaz") == 1)
print(Solution().countGoodSubstrings("aababcabc") == 4)