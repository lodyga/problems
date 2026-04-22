class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: iteration
        """
        s_freq = [0] * 26

        for char in s:
            idx = ord(char) - ord("a")
            s_freq[idx] += 1

        for char in t:
            idx = ord(char) - ord("a")
            s_freq[idx] -= 1

            if s_freq[idx] < 0:
                return char

        return ""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: bit manipulation
        """
        xor = 0

        for char in s:
            xor ^= ord(char) - ord("a")

        for char in t:
            xor ^= ord(char) - ord("a")

        return chr(xor + ord("a"))


print(Solution().findTheDifference("abcd", "abcde") == "e")
print(Solution().findTheDifference("", "y") == "y")
print(Solution().findTheDifference("a", "aa") == "a")
