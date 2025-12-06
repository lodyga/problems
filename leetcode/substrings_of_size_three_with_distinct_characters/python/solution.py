class Solution:
    def countGoodSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: hash set
            A: iteration
        """
        counter = 0
        for index in range(len(text) - 2):
            if len(set(text[index: index + 3])) == 3:
                counter += 1
        return counter


class Solution:
    def countGoodSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
            DS: hash map
            A: iteration
        """
        counter = 0
        letter_frequenty = {}
        left = 0
        
        for right, letter in enumerate(text):
            letter_frequenty[letter] = letter_frequenty.get(letter, 0) + 1

            if right - left < 2:
                continue

            if len(letter_frequenty) == 3:
                counter += 1
            left_letter = text[left]
            letter_frequenty[left_letter] -= 1
            if letter_frequenty[left_letter] == 0:
                letter_frequenty.pop(left_letter)
            left += 1
            
        return counter


print(Solution().countGoodSubstrings("xyzzaz") == 1)
print(Solution().countGoodSubstrings("aababcabc") == 4)
