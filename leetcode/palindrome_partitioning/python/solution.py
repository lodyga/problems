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
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if text[left] != text[right]:
                    return False
                left += 1
                right -= 1
            return True

        N = len(text)
        partitioned = []
        res = []

        def backtrack(start: int) -> None:
            if start == N:
                res.append(partitioned.copy())
                return

            for idx in range(start, N):
                if is_palindrome(start, idx):
                    partitioned.append(text[start: idx + 1])
                    backtrack(idx + 1)
                    partitioned.pop()
                
        backtrack(0)
        return res


print(Solution().partition("a") == [["a"]])
print(Solution().partition("aa") == [['a', 'a'], ['aa']])
print(Solution().partition("ab") == [["a", "b"]])
print(Solution().partition("aaa") == [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']])
print(Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]])
print(Solution().partition("aba") == [["a", "b", "a"], ["aba"]])
