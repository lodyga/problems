class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            DS: array
            A: sliding window
        """
        left = 0
        res = 0
        # ["a" counter, "b" counter, "c" counter]
        window = [0, 0, 0]

        for char in s:
            idx = ord(char) - ord("a")
            window[idx] += 1

            if not all(window):
                continue

            while left < len(s) and window[ord(s[left]) - ord("a")] > 1:
                window[ord(s[left]) - ord("a")] -= 1
                left += 1

            res += left + 1

        return res


print(Solution().numberOfSubstrings("abcabc") == 10)
print(Solution().numberOfSubstrings("aaacb") == 3)
print(Solution().numberOfSubstrings("abc") == 1)
