class Solution:
    def reverseString(self, letters: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: two pointers, iteration
        """
        left = 0
        right = len(letters) - 1

        while left < right:
            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1
        return letters


class Solution:
    def reverseString(self, letters: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O()
        Tags: two pointers, recursion
        """
        def dfs(left, right):
            if left < right:
                letters[left], letters[right] = letters[right], letters[left]
                dfs(left + 1, right - 1)

        dfs(0, len(letters) - 1)
        return letters


class Solution:
    def reverseString(self, letters: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: build-in function
        """
        letters.reverse()
        return letters


class Solution:
    def reverseString(self, letters: list[str]) -> list[str]:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        stack = []

        for letter in letters:
            stack.append(letter)

        for index in range(len(stack)):
            letters[index] = stack.pop()
        
        return letters


print(Solution().reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"])
print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"])