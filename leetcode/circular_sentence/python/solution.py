class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        for index in range(1, len(sentence) - 1):
            if (
                sentence[index] == " " and 
                sentence[index - 1] != sentence[index + 1]
            ):
                return False
        
        return sentence[0] == sentence[-1]


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: iteration, build-in function
        """
        words = sentence.split(' ')
        
        for index in range(len(words) - 1):
            word = words[index]
            next_word = words[index + 1]

            if word[-1] != next_word[0]:
                return False

        return words[-1][-1] == words[0][0]


print(Solution().isCircularSentence("leetcode exercises sound delightful") == True)
print(Solution().isCircularSentence("eetcode") == True)
print(Solution().isCircularSentence("Leetcode is cool") == False)
print(Solution().isCircularSentence("leetcode") == False)
print(Solution().isCircularSentence("MuFoevIXCZzrpXeRmTssj lYSW U jM") == False)
