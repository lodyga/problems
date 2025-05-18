class Solution:
    def partition(self, word: str) -> list[list[str]]:
        """
        Time complexity: O(n2^n)
        Auxiliary space complexity: O(2^n)
            Every dfs call contains new string
        Tags: iterative dfs with backtracking
        """
        partition = []
        partition_list = []

        def is_palindrome(left, right):
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start):
            if start == len(word):
                partition_list.append(partition.copy())
                return

            for index in range(start, len(word)):
                if is_palindrome(start, index):
                    partition.append(word[start: index + 1])
                    dfs(index + 1)
                    partition.pop()

        dfs(0)
        return partition_list


print(Solution().partition("a") == [["a"]])
print(Solution().partition("aa") ==  [['a', 'a'], ['aa']])
print(Solution().partition("ab") == [["a", "b"]])
print(Solution().partition("aaa") == [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']])
print(Solution().partition("aab") == [["a", "a", "b"], ["aa", "b"]])
print(Solution().partition("aba") == [["a", "b", "a"], ["aba"]])