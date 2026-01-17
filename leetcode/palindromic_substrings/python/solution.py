class Solution:
    def countSubstrings(self, text: str) -> int:
        """
        Time complexity: O(n2)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers
        """
        def count_palindromes(left, right):
            nonlocal counter
            while (
                left > -1 and
                right < len(text) and
                text[left] == text[right]
            ):
                counter += 1
                left -= 1
                right += 1

        counter = 0
        for index in range(len(text)):
            # check for odd length palindromes
            count_palindromes(index, index)
            # check for even length palindromes
            count_palindromes(index, index + 1)

        return counter


print(Solution().countSubstrings("abc") == 3)
print(Solution().countSubstrings("aaa") == 6)
