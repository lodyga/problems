class Solution:
    def reverseWords(self, text: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        """
        letter_list = []
        text_with_reversed_words = []

        for letter in text + " ":
            if letter == " ":
                text_with_reversed_words.extend(reversed(letter_list))
                text_with_reversed_words.append(" ")
                letter_list = []
            else:
                letter_list.append(letter)

        return "".join(text_with_reversed_words[:-1])


print(Solution().reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc")
print(Solution().reverseWords("Mr Ding") == "rM gniD")
print(Solution().reverseWords("hehhhhhhe") == "ehhhhhheh")