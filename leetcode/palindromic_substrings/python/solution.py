class Solution:
    def countSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        def count_palindromes(left, right):
            res = 0

            while (
                left > -1
                and right < len(text)
                and text[left] == text[right]
            ):
                res += 1
                left -= 1
                right += 1

            return res

        res = 0

        for idx in range(len(text)):
            # check for odd length palindromes
            res += count_palindromes(idx, idx)
            # check for even length palindromes
            res += count_palindromes(idx, idx + 1)

        return res


print(Solution().countSubstrings("abc") == 3)
print(Solution().countSubstrings("aaa") == 6)
