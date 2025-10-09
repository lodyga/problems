class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: iteration
        """
        last_letter = sentence[-1]
        was_space = True
        for letter in sentence:
            if was_space:
                if letter != last_letter:
                    return False
                was_space = False
            elif letter == " ":
                was_space = True
                continue
            last_letter = letter
        return True


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers
        """
        for index in range(1, len(sentence) - 1):
            if sentence[index] == " " and (sentence[index - 1] != sentence[index + 1]):
                return False
        return sentence[0] == sentence[-1]


print(Solution().isCircularSentence("leetcode exercises sound delightful") == True)
print(Solution().isCircularSentence("eetcode") == True)
print(Solution().isCircularSentence("Leetcode is cool") == False)
print(Solution().isCircularSentence("leetcode") == False)