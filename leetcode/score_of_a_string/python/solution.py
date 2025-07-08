class Solution:
    def scoreOfString(self, word: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: 
        """
        return sum(
            abs(ord(word[index - 1]) - ord(word[index]))
            for index in range(1, len(word))
        )


class Solution:
    def scoreOfString(self, word: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: 
        """
        points = [ord(letter) for letter in word]
        return sum(
            abs(points[index - 1] - points[index])
            for index in range(1, len(word))
        )


print(Solution().scoreOfString("hello") == 13)
print(Solution().scoreOfString("zaz") == 50)