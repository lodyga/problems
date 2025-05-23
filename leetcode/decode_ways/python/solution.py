r"""
draft
[2, 2, 6, 1]
 2  2  6  1
 2    26  1
 22    6  1
                  .
            /           \
           2            22
        /     \       /
       2      26     6
     /       /     /
    6       1     1
   /
  1

[3, 2, 1, 1, (1)]
{0: 3, 1: 2, 2: 1, 3: 1, 4: 1}
"""


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(1)
        Tags: dp, bottom-up
        """
        cache = [1, 1]

        for index in reversed(range(len(text))):
            if text[index] == "0":
                cache = [0, cache[0]]
                continue

            current_cache = cache[0]

            if (index + 1 < len(text) and
                    text[index: index + 2] <= "26"):
                current_cache += cache[1]

            cache = [current_cache, cache[0]]

        return cache[0]


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with cache as list
        """
        cache = [0] * (len(text) + 1)
        cache[-1] = 1

        for index in reversed(range(len(text))):
            if text[index] == "0":
                continue
            
            cache[index] = cache[index + 1]

            if (index + 1 < len(text) and
                    text[index: index + 2] <= "26"):
                cache[index] += cache[index + 2]

        return cache[0]


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, bottom-up with cache as hash map
        """
        cache = {len(text): 1}

        for index in reversed(range(len(text))):
            if text[index] == "0":
                cache[index] = 0
                continue
            
            cache[index] = cache[index + 1]

            if (index + 1 < len(text) and
                    text[index: index + 2] <= "26"):
                cache[index] += cache[index + 2]

        return cache[0]


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as hash map
        """
        memo = {len(text): 1}

        def dfs(index):
            if index in memo:
                return memo[index]
            elif text[index] == "0":
                return 0

            # choose one digit number
            memo[index] = dfs(index + 1)

            # choose two digit number
            if (index + 1 < len(text) and
                    text[index: index + 2] <= "26"):
                memo[index] += dfs(index + 2)

            return memo[index]

        return dfs(0)


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: dp, top-down with memoization as list
        """
        memo = [None] * (len(text) + 1)
        memo[-1] = 1

        def dfs(index):
            if memo[index] is not None:
                return memo[index]
            elif text[index] == "0":
                return 0

            # choose one digit number
            memo[index] = dfs(index + 1)

            # choose two digit number
            if (index + 1 < len(text) and
                    text[index: index + 2] <= "26"):
                memo[index] += dfs(index + 2)

            return memo[index]

        return dfs(0)


class Solution:
    def numDecodings(self, text: str) -> int:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags: brute-force, tle
        shared state
        """
        self.number_counter = 0

        def dfs(index):
            if index == len(text):
                self.number_counter += 1
                return
            elif text[index] == "0":
                return

            dfs(index + 1)
            if (index + 1 < len(text) and
                    text[index: index + 2] <= "26"):
                dfs(index + 2)

        dfs(0)
        return self.number_counter


print(Solution().numDecodings("5") == 1)
print(Solution().numDecodings("23") == 2)
print(Solution().numDecodings("226") == 3)
print(Solution().numDecodings("2261") == 3)
print(Solution().numDecodings("12") == 2)
print(Solution().numDecodings("2101") == 1)
print(Solution().numDecodings("06") == 0)
print(Solution().numDecodings("0") == 0)
print(Solution().numDecodings("111111111111111111111111111111111111111111111") == 1836311903)