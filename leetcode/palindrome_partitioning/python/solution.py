class Solution:
    def partition(self, text: str) -> list[list[str]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(n)
            Output: O(2^n)
        Tags: 
            DS: list
            A: DFS with backtracking
        """
        def is_palindromes(left: int, right: int) -> bool:
            while left < right:
                if text[left] != text[right]:
                    return False
                left += 1
                right -= 1
            return True

        palindrome = []
        palindrome_list = []

        def backtrack(index: int) -> None:
            if index == len(text):
                palindrome_list.append(palindrome.copy())
                return

            for right in range(index, len(text)):
                if is_palindromes(index, right):
                    palindrome.append(text[index: right + 1])
                    backtrack(right + 1)
                    palindrome.pop()

        backtrack(0)
        return palindrome_list


print(Solution().partition("a") == [["a"]])
print(Solution().partition("aa") == [['a', 'a'], ['aa']])
print(Solution().partition("ab") == [["a", "b"]])
print(Solution().partition("aaa") == [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']])
print(Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]])
print(Solution().partition("aba") == [["a", "b", "a"], ["aba"]])
