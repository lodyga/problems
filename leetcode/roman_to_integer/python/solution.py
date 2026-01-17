r"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    def romanToInt(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
        """
        number = 0
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for index, letter in enumerate(text):
            number += value_map[letter]

            if index + 1 == len(text):
                continue
            
            next_letter = text[index + 1]

            if (
                (letter == "I" and next_letter in "VX") or 
                (letter == "X" and next_letter in "LC") or 
                (letter == "C" and next_letter in "DM")
            ):
                number -= 2*value_map[letter]
        
        return number


class Solution:
    def romanToInt(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
        """
        number = 0
        value_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        index = 0
        while index < len(text):
            letter = text[index]
            if index + 1 == len(text):
                number += value_map[letter]
                break

            next_letter = text[index + 1]
            if value_map[letter] < value_map[next_letter]:
                number += -value_map[letter] + value_map[next_letter]
                index += 2
            else:
                number += value_map[letter]
                index += 1
            
        return number


print(Solution().romanToInt("III") == 3)
print(Solution().romanToInt("IV") == 4)
print(Solution().romanToInt("V") == 5)
print(Solution().romanToInt("VI") == 6)
print(Solution().romanToInt("IX") == 9)
print(Solution().romanToInt("X") == 10)
print(Solution().romanToInt("XII") == 12)
print(Solution().romanToInt("LVIII") == 58)
print(Solution().romanToInt("MCMXCIV") == 1994)