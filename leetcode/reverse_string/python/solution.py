class Solution:
    def reverseString(self, letters: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: build-in function
        """
        return list(reversed(letters))


class Solution:
    def reverseString(self, letters: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags:
            A: two pointers, iteration
        """
        res = letters.copy()
        left = 0
        right = len(letters) - 1

        while left < right:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

        return res


class Solution:
    def reverseString(self, letters: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            A: two pointers, recursion
        """
        def dfs(left, right):
            if left >= right:
                return

            letters[left], letters[right] = letters[right], letters[left]
            dfs(left + 1, right - 1)

        dfs(0, len(letters) - 1)
        return letters


print(Solution().reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"])
print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"])
